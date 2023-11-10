import plotly.graph_objs as goh
import yfinance as yif
print("welcome to Stonks")
print("\nWhich stocks data would you like to request?")
print("\n1. Google")
print("\n2. Tesla")
print("\n3. Apple")
print("\n4. Cisco")
print("\n5. Intel")
print("\n6. Name your own stock")
ch = input("\nPlease enter your choice.\n")
if ch == "1":
    print(ch)
    data = yif.download(tickers="GOOG", period="5d", interval="1h", rounding=True)
    fig = goh.Figure()
    fig.add_trace(
        goh.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'],
                        name='market data'))
    fig.update_layout(title='Google share price', yaxis_title='Stock Price (Rs)')
    fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(buttons=list([
        dict(count=15, label='15m', step='minute', stepmode='backward'),
        dict(count=45, label='45m', step='minute', stepmode='backward'),
        dict(count=1, label='1h', step='hour', stepmode='backward'),
        dict(count=6, label='6h', step='hour', stepmode='backward'),
        dict(step='all')])))
    fig.show()

elif ch == "2":
    data = yif.download(tickers="TSLA", period="5d", interval="1h", rounding=True)
    fig = goh.Figure()
    fig.add_trace(
        goh.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'],
                        name='market data'))
    fig.update_layout(title='Tesla share price', yaxis_title='Stock Price (USD)')
    fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(buttons=list([
        dict(count=15, label='15m', step='minute', stepmode='backward'),
        dict(count=45, label='45m', step='minute', stepmode='backward'),
        dict(count=1, label='1h', step='hour', stepmode='backward'),
        dict(count=6, label='6h', step='hour', stepmode='backward'),
        dict(step='all')])))
    fig.show()

elif ch == "3":
    data = yif.download(tickers="APPL", period="5d", interval="1h", rounding=True)
    fig = goh.Figure()
    fig.add_trace(
        goh.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'],
                        name='market data'))
    fig.update_layout(title='Apple share price', yaxis_title='Stock Price (USD)')
    fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(buttons=list([
        dict(count=15, label='15m', step='minute', stepmode='backward'),
        dict(count=45, label='45m', step='minute', stepmode='backward'),
        dict(count=1, label='1h', step='hour', stepmode='backward'),
        dict(count=6, label='6h', step='hour', stepmode='backward'),
        dict(step='all')])))
    fig.show()

elif ch == "4":
    data = yif.download(tickers="CSCO", period="5d", interval="1h", rounding=True)
    fig = goh.Figure()
    fig.add_trace(
        goh.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'],
                        name='market data'))
    fig.update_layout(title='Cisco share price', yaxis_title='Stock Price (USD)')
    fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(buttons=list([
        dict(count=15, label='15m', step='minute', stepmode='backward'),
        dict(count=45, label='45m', step='minute', stepmode='backward'),
        dict(count=1, label='1h', step='hour', stepmode='backward'),
        dict(count=6, label='6h', step='hour', stepmode='backward'),
        dict(step='all')])))
fig.show()

elif ch == "5":
    data = yif.download(tickers="INTC", period="5d", interval="1h", rounding=True)
    fig = goh.Figure()
    fig.add_trace(
        goh.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'],
                        name='market data'))
    fig.update_layout(title='Intel share price', yaxis_title='Stock Price (USD)')
    fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(buttons=list([
        dict(count=15, label='15m', step='minute', stepmode='backward'),
        dict(count=45, label='45m', step='minute', stepmode='backward'),
        dict(count=1, label='1h', step='hour', stepmode='backward'),
        dict(count=6, label='6h', step='hour', stepmode='backward'),
        dict(step='all')])))
    fig.show()

elif ch == "6":
    na = input("Enter stock name")
    data = yif.download(tickers=na, period="5d", interval="1h", rounding=True)
    
fig = goh.Figure()
    fig.add_trace(
        


goh.Candlestick(x=data.index, open=data['Open'], high=data['High'], low=data['Low'], close=data['Close'],
                        name='market data'))
    fig.update_layout(title=na+' share price', yaxis_title='Stock Price (Rs)')
    fig.update_xaxes(rangeslider_visible=True, rangeselector=dict(buttons=list([
        dict(count=15, label='15m', step='minute', stepmode='backward'),
        dict(count=45, label='45m', step='minute', stepmode='backward'),
        dict(count=1, label='1h', step='hour', stepmode='backward'),
        dict(count=6, label='6h', step='hour', stepmode='backward'),
        dict(step='all')])))
    fig.show()
