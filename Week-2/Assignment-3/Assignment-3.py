def avg(data):
# your code here
    tol_price = 0
    for i in range(len(data['products'])):
        tol_price += data['products'][i]['price']
    ans = round(tol_price/len(data['products']),3)
    return ans
print(
avg({
"products": [
{
"name": "Product 1",
"price": 100
},
{
"name": "Product 2",
"price": 700
},
{
"name": "Product 3",
"price": 300
}
]
})
)
# print the average price of all products (round to 3 decimal)
# ans = 366.667