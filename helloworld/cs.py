import datetime  #
import os.path  # 路径管理
import sys  # 获取当前运行脚本的路径 (in argv[0])
import backtrader.feeds as btfeed
# 导入backtrader框架
import backtrader as bt


class BSCSVData(btfeed.GenericCSVData):
    params = (
        ("fromdate", datetime.datetime(2020, 12, 1)),
        ("todate", datetime.datetime(2021, 12, 1)),
        ('dtformat', ('%Y-%m-%d')),
        ('openinterest', -1)
    )

# 创建策略继承bt.Strategy
class TestStrategy(bt.Strategy):

    def log(self, txt, dt=None):
        # 记录策略的执行日志
        dt = dt or self.datas[0].datetime.date(0)
        print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # 保存收盘价的引用
        self.dataclose = self.datas[0].close
        self.dataopen = self.datas[0].open
        self.sma15 = bt.indicators.SimpleMovingAverage(
            self.datas[0], period=15)
        self.sma5 = bt.indicators.SimpleMovingAverage(
            self.datas[0], period=5)
        self.sma10 = bt.indicators.SimpleMovingAverage(
            self.datas[0], period=10)
        # 跟踪挂单
        self.order = None
        # bt.indicators.ExponentialMovingAverage(self.datas[0], period=25)
        # bt.indicators.WeightedMovingAverage(self.datas[0], period=25).subplot = True
        # bt.indicators.StochasticSlow(self.datas[0])
        # bt.indicators.MACDHisto(self.datas[0])
        # rsi = bt.indicators.RSI(self.datas[0])
        # bt.indicators.SmoothedMovingAverage(rsi, period=10)
        # bt.indicators.ATR(self.datas[0]).plot = False

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # broker 提交/接受了，买/卖订单则什么都不做
            return

        # 检查一个订单是否完成
        # 注意: 当资金不足时，broker会拒绝订单
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log('已买入, %.2f' % order.executed.price)
            elif order.issell():
                self.log('已卖出, %.2f' % order.executed.price)

            # 记录当前交易数量
            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('订单取消/保证金不足/拒绝')

        # 其他状态记录为：无挂起订单
        self.order = None

    def next(self):
        # 记录收盘价
        self.log('Close, %.2f' % self.dataclose[0])

        # 如果有订单正在挂起，不操作
        if self.order:
            return

        #逻辑1
        # 如果没有持仓则买入
        if not self.position:
            # 今天的开盘价 > 昨天收盘价
            if self.dataopen[0] > self.dataclose[-1]:
                # 买入
                self.log('买入, %.2f' % self.dataclose[0])
                # 跟踪订单避免重复
                self.order = self.buy(size=1000,price=self.dataopen[0]+0.01)
        else:
            # 今天的开盘价 < 昨天收盘价
            if self.dataopen[0] < self.dataclose[-2]:
                # 卖出
                self.log('卖出, %.2f' % self.dataclose[0])
                # 跟踪订单避免重复
                self.order = self.sell(size=1000,price=self.dataopen[0]-0.01)
            else:
                # 买入
                self.log('买入, %.2f' % self.dataclose[0])
                # 跟踪订单避免重复
                self.order = self.buy(size=1000,price=self.dataopen[0]+0.01)
        #逻辑2
        # 如果没有持仓则买入
        # if not self.position:
        #     # 今天的开盘价 > 昨天收盘价
        #     if ((self.dataopen[0] - self.dataclose[-1]) / self.dataclose[-1]) >= 0.01 and (
        #             (self.dataopen[0] - self.dataclose[-1]) / self.dataclose[-1]) <= 0.02:
        #         # 买入
        #         self.log('买入, %.2f' % self.dataclose[0])
        #         # 跟踪订单避免重复
        #         self.order = self.buy(size=1000, price=self.dataopen[0] + 0.01)
        # else:
        #     # 今天的开盘价 < 前天收盘价
        #     if ((self.dataopen[0] - self.dataclose[-2]) / self.dataclose[-2]) <= -0.03:
        #         # 卖出
        #         self.log('卖出, %.2f' % self.dataclose[0])
        #         # 跟踪订单避免重复
        #         self.order = self.sell(size=1000,price=self.dataopen[0]-0.01)
        #     elif ((self.dataopen[0] - self.dataclose[-2]) / self.dataclose[-2]) >= 0.1:
        #         # 卖出
        #         self.log('卖出, %.2f' % self.dataclose[0])
        #         # 跟踪订单避免重复
        #         self.order = self.sell(size=1000,price=self.dataopen[0]-0.01)
        #     elif ((self.dataopen[0] - self.dataclose[-1]) / self.dataclose[-1]) >= 0.01 and (
        #             (self.dataopen[0] - self.dataclose[-1]) / self.dataclose[-1]) <= 0.02:
        #         # 买入
        #         self.log('买入, %.2f' % self.dataclose[0])
        #         # 跟踪订单避免重复
        #         self.order = self.buy(size=1000, price=self.dataopen[0] + 0.01)
        # # # 逻辑3
        # # 如果没有持仓则买入
        # zuo1 = self.dataclose[-1]
        # zuo2 = self.dataclose[-2]
        # zuo3 = self.dataclose[-3]
        # zuo4 = self.dataclose[-4]
        # zuo5 = self.dataclose[-5]
        # zuo6 = self.dataclose[-6]
        # zuo7 = self.dataclose[-7]
        # zuo8 = self.dataclose[-8]
        # zuo9 = self.dataclose[-9]
        # zuo10 = self.dataclose[-10]
        # pin5=(zuo1+zuo2+zuo3+zuo4+zuo5)/5
        # pin10=(zuo1+zuo2+zuo3+zuo4+zuo5+zuo6+zuo7+zuo8+zuo9+zuo10)/10
        # pinj5=("%.2f" % pin5)
        # pinj10 = ("%.2f" % pin10)
        # if not self.position:
        #     # 今天的开盘价 > 昨天收盘价
        #     if ((self.dataopen[0] - self.dataclose[-1]) / self.dataclose[-1]) < -0.03:
        #         # 买入
        #         self.log('买入, %.2f' % self.dataclose[0])
        #         # 跟踪订单避免重复
        #         self.order = self.buy(size=10000, price=self.dataopen[0] + 0.01)
        # else:
        #     # 今天的开盘价 < 前天收盘价
        #     if ((self.dataopen[0] - self.dataclose[-2]) / self.dataclose[-2]) >= 0.1 or ((self.dataopen[0] - self.dataclose[-1]) / self.dataclose[-1]) >= 0.05:
        #         # 卖出
        #         self.log('卖出, %.2f' % self.dataclose[0])
        #         # 跟踪订单避免重复
        #         self.order = self.sell(size=1000, price=self.dataopen[0] - 0.01)
        #     elif ((self.dataopen[0] - self.dataclose[-1]) / self.dataclose[-1]) <= -0.03 or ((self.dataopen[0] - self.dataclose[-2]) / self.dataclose[-2]) <= -0.1:
        #         # 买入
        #         self.log('买入, %.2f' % self.dataclose[0])
        #         # 跟踪订单避免重复
        #         self.order = self.buy(size=1000, price=self.dataopen[0] + 0.01)
        # 逻辑4
        # 如果没有持仓则买入
        # print('当前可用资金', self.broker.getcash())
        # print('当前总资产', self.broker.getvalue())
        # print('当前持仓量', self.broker.getposition(self.data).size)
        # print('当前持仓成本', self.broker.getposition(self.data).price)
        # zuo1=self.dataclose[-1]
        # zuo2 = self.dataclose[-2]
        # zuo3 = self.dataclose[-3]
        # zuo4 = self.dataclose[-4]
        # zuo5 = self.dataclose[-5]
        # zuo6 = self.dataclose[-6]
        # zuo7 = self.dataclose[-7]
        # zuo8 = self.dataclose[-8]
        # zuo9 = self.dataclose[-9]
        # zuo10 = self.dataclose[-10]
        # pin5=(zuo1+zuo2+zuo3+zuo4+zuo5)/5
        # pin10=(zuo1+zuo2+zuo3+zuo4+zuo5+zuo6+zuo7+zuo8+zuo9+zuo10)/10
        # pinj5=("%.2f" % pin5)
        # pinj10 = ("%.2f" % pin10)
        # if not self.position:
        #     if zuo10<zuo1*1.05 and pinj5<pinj10:
        #         # 买入
        #         self.log('买入, %.2f' % self.dataclose[0])
        #         # 跟踪订单避免重复
        #         self.order = self.buy(size=10000, price=zuo1 + 0.01)
        # else:
        #     if zuo10*1.1<zuo1:
        #         # 卖出
        #         self.log('卖出, %.2f' % self.dataclose[0])
        #         # 跟踪订单避免重复
        #         self.order = self.sell(size=10000, price=self.dataopen[0] - 0.01)
        #     elif zuo10<zuo1*1.05 and pinj5<pinj10:
        #         # 买入
        #         self.log('买入, %.2f' % self.dataclose[0])
        #         # 跟踪订单避免重复
        #         self.order = self.buy(size=10000, price=zuo1 + 0.01)

        # # 逻辑5
        # 如果没有持仓则买入
        # zuo1 = self.dataclose[-1]
        # zuo2 = self.dataclose[-2]
        # zuo3 = self.dataclose[-3]
        # zuo4 = self.dataclose[-4]
        # zuo5 = self.dataclose[-5]
        # zuo6 = self.dataclose[-6]
        # zuo7 = self.dataclose[-7]
        # zuo8 = self.dataclose[-8]
        # zuo9 = self.dataclose[-9]
        # zuo10 = self.dataclose[-10]
        # zuo11 = self.dataclose[-11]
        # zuo12 = self.dataclose[-12]
        # pin5 = (zuo1 + zuo2 + zuo3 + zuo4 + zuo5) / 5
        # pin10 = (zuo1 + zuo2 + zuo3 + zuo4 + zuo5 + zuo6 + zuo7 + zuo8 + zuo9 + zuo10) / 10
        # ping5= (zuo3 + zuo4 + zuo5 + zuo6 + zuo7) / 5
        # ping10 = (zuo3 + zuo4 + zuo5 + zuo6 + zuo7 + zuo8 + zuo9 + zuo10 + zuo11 + zuo12) / 10
        # ping25 = (zuo2 + zuo3 + zuo4 + zuo5 + zuo6) / 5
        # ping210 = (zuo3 + zuo4 + zuo5 + zuo6 + zuo7 + zuo8 + zuo9 + zuo10 + zuo11 + zuo2) / 10
        # pin1 = ("%.2f" % pin5)
        # pin2 = ("%.2f" % pin10)
        # pin5 = ("%.2f" % ping5)
        # pin6 = ("%.2f" % ping10)
        # pin3 = ("%.2f" % ping25)
        # pin4 = ("%.2f" % ping210)
        # keyong=self.broker.getcash()
        # aa = (self.dataopen[0] + self.dataclose[0]) / 2
        # bb = float(("%.2f" % aa))
        # xx=int(keyong/bb/100)*100
        # print(xx)
        # if not self.position:
        #     # 今天的开盘价 > 昨天收盘价
        #     if pin1<pin2 and pin5<pin3 and pin3<pin1 and pin6>pin4 and pin4>pin2:
        #         # 买入
        #         self.log('买入, %.2f' % self.dataclose[0])
        #         # 跟踪订单避免重复
        #         self.order = self.buy(size=xx, price=bb)
        # else:
        #     # 今天的开盘价 < 前天收盘价
        #     if pin1>pin2 and pin5>pin3 and pin3>pin1 and pin6<pin4 and pin4<pin2:
        #         # 卖出
        #         self.log('卖出, %.2f' % self.dataclose[0])
        #         # 跟踪订单避免重复
        #         self.order = self.sell(size=self.broker.getposition(self.data).size, price=bb)
        #     elif pin1<pin2 and pin5<pin3 and pin3<pin1 and pin6>pin4 and pin4>pin2:
        #         # 买入
        #         self.log('买入, %.2f' % self.dataclose[0])
        #         # 跟踪订单避免重复
        #         self.order = self.buy(size=xx, price=bb)
        # # 逻辑5
        # # 如果没有持仓则买入
        # zuo1 = self.dataclose[-1]
        # zuo2 = self.dataclose[-2]
        # zuo3 = self.dataclose[-3]
        # zuo4 = self.dataclose[-4]
        # zuo5 = self.dataclose[-5]
        # zuo6 = self.dataclose[-6]
        # zuo7 = self.dataclose[-7]
        # zuo8 = self.dataclose[-8]
        # zuo9 = self.dataclose[-9]
        # zuo10 = self.dataclose[-10]
        # zuo11 = self.dataclose[-11]
        # zuo12 = self.dataclose[-12]
        # pin5 = (zuo1 + zuo2 + zuo3 + zuo4 + zuo5) / 5
        # pin10 = (zuo1 + zuo2 + zuo3 + zuo4 + zuo5 + zuo6 + zuo7 + zuo8 + zuo9 + zuo10) / 10
        # ping5 = (zuo3 + zuo4 + zuo5 + zuo6 + zuo7) / 5
        # ping10 = (zuo3 + zuo4 + zuo5 + zuo6 + zuo7 + zuo8 + zuo9 + zuo10 + zuo11 + zuo12) / 10
        # ping25 = (zuo2 + zuo3 + zuo4 + zuo5 + zuo6) / 5
        # ping210 = (zuo3 + zuo4 + zuo5 + zuo6 + zuo7 + zuo8 + zuo9 + zuo10 + zuo11 + zuo2) / 10
        # pin1 = ("%.2f" % pin5)
        # pin2 = ("%.2f" % pin10)
        # pin5 = ("%.2f" % ping5)
        # pin6 = ("%.2f" % ping10)
        # pin3 = ("%.2f" % ping25)
        # pin4 = ("%.2f" % ping210)
        # keyong = self.broker.getcash()
        # aa = self.dataopen[0]
        # bb = float(("%.2f" % aa))
        # cc=float(("%.2f" % self.sma5[0]))
        # xx = int(keyong / bb / 100) * 100
        # print(self.dataclose[0])
        # print(self.sma5[0])
        # if not self.position:
        #
        #     # 还没买，如果 MA5 > MA10 说明涨势，买入
        #     if self.dataclose[0] >= self.sma5[0]:
        #         self.log('BUY CREATE, %.2f' % self.dataclose[0])
        #         self.order = self.buy(size=xx, price=cc)
        #
        # else:
        #     if self.dataclose[0] >= self.sma5[0]:
        #         self.log('BUY CREATE, %.2f' % self.dataclose[0])
        #         self.order = self.buy(size=xx, price=cc)
        #     # 已经买了，如果 MA5 < MA10 ，说明跌势，卖出
        #     elif self.dataclose[0] < self.sma5[0]:
        #         self.log('SELL CREATE, %.2f' % self.dataclose[0])
        #         self.order = self.sell(size=self.broker.getposition(self.data).size, price=cc)


            # # 如果已经持仓，且当前交易数据量在买入后5个单位后
            # if len(self) >= (self.bar_executed + 5):
            #     # 全部卖出
            #     self.log('卖出, %.2f' % self.dataclose[0])
            #     # 跟踪订单避免重复
            #     self.order = self.sell(size=1000)



if __name__ == '__main__':
    # 创建Cerebro引擎
    cerebro = bt.Cerebro()
    # Cerebro引擎在后台创建broker(经纪人)，系统默认资金量为10000

    # 为Cerebro引擎添加策略
    cerebro.addstrategy(TestStrategy)

    # 获取当前运行脚本所在目录
    modpath = os.path.dirname(os.path.abspath(sys.argv[0]))
    # 拼接加载路径
    datapath = os.path.join(modpath, '../../datas/orcl-1995-2014.txt')

    filename = 'bs_sz.300373.csv'

    # 创建交易数据集
    data = BSCSVData(dataname="../datas/{0}".format(filename))

    # 加载交易数据
    cerebro.adddata(data)

    # 设置投资金额100000.0
    cerebro.broker.setcash(10000000.0)

    # 设置佣金
    #cerebro.broker.setcommission(0.003)
    # 引擎运行前打印期出资金
    print('组合期初资金: %.2f' % cerebro.broker.getvalue())
    cerebro.run()
    # 引擎运行后打期末资金
    print('组合期末资金: %.2f' % cerebro.broker.getvalue())
    #cerebro.plot()