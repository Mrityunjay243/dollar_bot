# Added feature that automatically converts from any given currency to USD
Since the application was only limited to USD which restricted its usage and application we added a feature where the user can specify the three character currency code after any monetary entry and it'll be automatically converted to USD.

`convertCurrency(amount, from_currency):`
This function is called to convert the amount specified from the specified currency to USD. We have used the Open Exchange Rates API to get the latest data on current currency exchange rates. 