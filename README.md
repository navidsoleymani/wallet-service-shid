# Wallet Service
این سیستم برای مدیریت تراکنش های مالی ساخته شده است که دارای توابع زیر می باشد که در رابطه با هرکدام به تفضیل توضیح داده می شود.

## Wallet Transaction 
این تابع یک تراکنش مالی را ثبت می کند و در جیب متناسب با کیف پول کاربر مورد نظر قرار می گیرد مسیر دسترسی آن و ورودی ها و خروجی این تابع به صورت زیر تعریف می شود.

```
URL: [localhost]/wallet/wallet/wallet/transaction/new/

Method: POST
{
    "actions": {
        "POST": {
            "id": {
                "type": "string",
                "required": false,
                "read_only": true,
                "label": "Id"
            },
            "date": {
                "type": "datetime",
                "required": false,
                "read_only": true,
                "label": "Date"
            },
            "amount": {
                "type": "float",
                "required": true,
                "read_only": false,
                "label": "Amount"
            },
            "transaction_information": {
                "type": "field",
                "required": false,
                "read_only": false,
                "label": "Transaction information"
            },
            "wallet": {
                "type": "field",
                "required": true,
                "read_only": false,
                "label": "Wallet"
            }
        }
    }
}
```
## Get Wallet Transaction List
این تابع لیست تمام تراکنش های مربوط به کیف پول ها را بر می گرداند.


```
URL: [localhost]/wallet/wallet/wallet/transaction/list/

Method: GET

```
## Create Wallet
این تابع برای ساختن یک کیف پول با جیب های مختلف برای کار می باشد. به این صورت که از این تابع استفاده کرده و مقدار یوزر آیدی و نام جیب مورد نظر را به تابع می دهیم تا کیف پول و جیب هایش را برایمان بسازد.
```
URL: [localhost]/wallet/wallet/wallet/new/

Method: POST
{
    "actions": {
        "POST": {
            "id": {
                "type": "string",
                "required": false,
                "read_only": true,
                "label": "Id"
            },
            "user_id": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "User id"
            },
            "pocket_name": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "Pocket name",
                "max_length": 128
            },
            "balance": {
                "type": "float",
                "required": false,
                "read_only": true,
                "label": "Balance"
            },
            "is_block": {
                "type": "boolean",
                "required": false,
                "read_only": true,
                "label": "Is block"
            }
        }
    }
}
```
## Get Wallet List
این تابع برای دریافت لیست تمام کیف پول ها استفاده می شود.

```
URL: [localhost]/wallet/wallet/wallet/list/

Method: GET

```
## Your Pocket Transaction
این تابع برای دریافت تراکنش های مربوط به 'جیب تو' ساخته شده است و تراکنش های مربوط را ثبت و تغیرات را اعمال می نماید.

```
URL: [localhost]/wallet/wallet/your-pocket/transaction/new/

Method: POST
{
    "actions": {
        "POST": {
            "id": {
                "type": "string",
                "required": false,
                "read_only": true,
                "label": "Id"
            },
            "date": {
                "type": "datetime",
                "required": false,
                "read_only": true,
                "label": "Date"
            },
            "amount": {
                "type": "float",
                "required": true,
                "read_only": false,
                "label": "Amount"
            },
            "transaction_information": {
                "type": "field",
                "required": false,
                "read_only": false,
                "label": "Transaction information"
            },
            "your_pocket": {
                "type": "field",
                "required": true,
                "read_only": false,
                "label": "Your pocket"
            }
        }
    }
}
```
## Get Your Pocket Transaction List
این تابع برای دریافت لیست تمام تراکنش های مربوط به جیب تو ها استفاده می شود.
```
URL: [localhost]/wallet/wallet/your-pocket/transaction/list/

Method: GET

```
## Get Your Pocket Transaction Details
این تابع برای دریافت جزئیات مربوط به تراکنش های جیب تو استفاده می شود.
```
URL: [localhost]/wallet/wallet/your-pocket/transaction/<transaction_id>/detail/

Method: GET

```
## Create Your Pocket
این تابع برای ساخت جیب تو استفاده می شود. به این صورت که یک یوزر آدی دریافت می کند و در صورتی که جیب تو ی فعالی برای کاربر مورد نظر موجود نباشد یک جیب تو برای آن می سازد و زمان فعال بودن آن را تا سی روز دیگر مشخص می کند.

```
URL: [localhost]/wallet/wallet/your-pocket/new/

Method: POST

{
    "actions": {
        "POST": {
            "id": {
                "type": "string",
                "required": false,
                "read_only": true,
                "label": "Id"
            },
            "user_id": {
                "type": "string",
                "required": true,
                "read_only": false,
                "label": "User id"
            },
            "balance": {
                "type": "float",
                "required": false,
                "read_only": true,
                "label": "Balance"
            },
            "active": {
                "type": "boolean",
                "required": false,
                "read_only": true,
                "label": "Active"
            },
            "expiry_date": {
                "type": "datetime",
                "required": false,
                "read_only": true,
                "label": "Expiry date"
            },
            "your_pocket_information": {
                "type": "field",
                "required": true,
                "read_only": false,
                "label": "Your pocket information"
            }
        }
    }
}
```
## Get Your Pocket List
این تابع لیست تمام جیب تو های فعال را بر میگرداند.
```
URL: [localhost]/wallet/wallet/your-pocket/list/

Method: GET

```
## Get All Transaction
این تابع لیست تمام تراکنش های موجود را بر میگرداند.
```
URL: [localhost]/wallet/wallet/all/transaction/list/

Method: GET

```


# Setting
 در این اپ شما می توانید مقدار مینیمم و ماکزیمم برای تراکنش ها انتخاب کنید و یا یک کیف پول را فعال یا بلاک نمایید.
 
## Set Max and Min
تعیین مقدار بالا و پایین برای تراکنش ها.

```
URL: [localhost]/setting/transaction/set/minmax/

Method: GET

{
    "actions": {
        "GET": {
            "maximum": {
                "type": "bool",
                "required": true,
                "read_only": true,
                "label": "maximum"
            },
            
            "minimum": {
                "type": "bool",
                "required": true,
                "read_only": true,
                "label": "minimum"
            }
        }
    }
}
```


## Block Wallet
بلاک کردن کیف پول مورد نظر.
```
URL: [localhost]/setting/wallet/block/

Method: GET

{
    "actions": {
        "GET": {
            "wallet_id": {
                "type": "char",
                "required": true,
                "read_only": true,
                "label": "wallet_id"
            }
        }
    }
}
```

## Unblock Wallet
فعال کردن کیف پول مورد نظر.
```
URL: [localhost]/setting/wallet/unblock/

Method: GET

{
    "actions": {
        "GET": {
            "wallet_id": {
                "type": "char",
                "required": true,
                "read_only": true,
                "label": "wallet_id"
            }
        }
    }
}
```