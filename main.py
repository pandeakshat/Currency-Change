
import streamlit as st 



def dpMakeChange(coinValueList,change,mincoins,coinsUsed):
    for counts in range(change+1):
        coinCount = counts
        newcoin = 1
        for j in [c for c in coinValueList if c <= counts]:
            if mincoins[counts-j] + 1 < coinCount:
                coinCount = mincoins[counts-j]+1
                newcoin = j
            mincoins[counts] = coinCount
            coinsUsed[counts] = newcoin
    return str(mincoins[change])



def printcoins(coinsUsed,change,coin_list):
    coin = change
    while coin > 0:
        thiscoin = coinsUsed[coin]
        coin_list.append(thiscoin)
        coin = coin - thiscoin

def main():
    st.title("Currency Change Program")
    Total=int(st.number_input('Enter Amount Paid:',1))
    cost=int(st.slider('Enter Cost', 0, Total))
    amnt = Total-cost
    curr=st.selectbox('Pick one', ['Indian Rupee - ₹', 'British Pound - £','American Dollar - $',"European Euro - €","Chinese Yuan - ㍐","Japanese Yen - ¥"])
    if(curr=="Indian Rupee - ₹"): clist = [1,2,5,10,20,50,100,200,500,2000]; 
    if(curr=="British Pound - £"): clist = [1,2,5,10,20,50]; 
    if(curr=="American Dollar - $"): clist = [1,2,5,10,20,50,100]; 
    if(curr=="European Euro - €"): clist=[1,2,5,10,20,50,100,200,500]; 
    if(curr=="Chinese Yuan - ㍐"): clist=[1,2,5,10,20,50,100]; 
    if(curr=="Japanese Yen - ¥"): clist=[1,5,10,50,100,500,1000,2000,5000,10000]; 
    
    coinsUsed = [0]*(amnt+1)
    coinCount= [0]*(amnt+1)
    coin_list=[]
    st.write("Change to give = ",curr.split('-')[-1],str(amnt))
    st.write("Making change of",curr.split('-')[-1],str(amnt),"requires " + dpMakeChange(clist,amnt,coinCount,coinsUsed),"units of currency")
    st.write("They are:")
    printcoins(coinsUsed,amnt,coin_list)
    coin_change = {item:coin_list.count(item) for item in coin_list}
    for coin,value in coin_change.items():
        st.write( curr.split('-')[-1] + str(coin) + " x " + str(value) )    
    st.markdown("""
    <div style="display: flex; justify-content: center; align-items: center; flex-direction: column;">
        <hr>
        <p style="text-align: center;">Akshat Pande - Currency Change</p>
    </div>
""", unsafe_allow_html=True)
main()