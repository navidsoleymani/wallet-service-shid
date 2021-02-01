def translator(message: dict):
    from wallet_service.settings import LANGUAGE_CODE
    if LANGUAGE_CODE in message.keys():
        return message[LANGUAGE_CODE]
    return message['en-us']


TRANSACTION_ALLOWED = translator(
    {
        "en-us": "The transaction was successful.",
        "fa-ir": "تراکنش با موفقیت انجام شد.",
    }
)
YOUR_POCKET_IS_NOT_ACTIVE = translator(
    {
        "en-us": "Wallet (your pocket) is disabled.",
        "fa-ir": "کیف پول جیب تو غیر فعال می باشد.",
    }
)
CREATE_WALLET = translator(
    {
        "en-us": "Wallet definition for user was successfully completed.",
        "fa-ir": "تعریف کیف پول برای کاربر مورد نظر با موفقیت انجام شد.",
    }
)
CREATE_YOUR_POCKET = translator(
    {
        "en-us": "Wallet (your pocket) was successfully defined.",
        "fa-ir": "کیف پول (جیب تو) با موفقیت تعریف شد.",
    }
)
SET_TRANSACTION_LIMIT = translator(
    {
        "en-us": "Bank transaction restrictions were successfully adjusted.",
        "fa-ir": "محدودیت های تراکنش های بانکی با موفقیت تنظیم شد.",
    }
)
SET_EXPIRY_DATE = translator(
    {
        "en-us": "The validity period of the wallet (your pocket) in the desired system was successfully set.",
        "fa-ir": "مدت اعتبار کیف پول (جیب تو) در سامانه مورد نظر با موفقیت تنظیم شد.",
    }
)
TYPE_IS_NOT_TRUE = translator(
    {
        "en-us": "The specified typo is incorrect. Each transaction is either 'wallet' or 'your_pocket'.",
        "fa-ir": "تایپ مشخص شده اشتباه است. هر تراکنش یا مربوط به 'wallet' است یا مربوط به 'your_pocket' است.",
    }
)

TRANSACTION_TRUE = translator(
    {
        "en-us": "The transaction was successfully executed.",
        "fa-ir": "تراکنش مورد نظر با موفقیت اعمال شد.",
    }
)

TRANSACTION_FALSE = translator(
    {
        "en-us": "The transaction encountered a problem.",
        "fa-ir": "تراکنش مورد نظر با مشکل مواجه شد.",
    }
)

WALLET_LIST = translator(
    {
        "en-us": "A list of all available wallets is displayed.",
        "fa-ir": "لیست تمام کیف پول های موجود، نمایش داده شد.",
    }
)

WALLET_LIST_POCKET_NAME = translator(
    {
        "en-us": "A list of all available wallets is displayed by wallet name.",
        "fa-ir": "لیست تمام کیف پول های موجود بر اساس نام کیف پول، نمایش داده شد.",
    }
)

YOUR_POCKET_LIST = translator(
    {
        "en-us": "A list of all available wallet(your pocket)s is displayed.",
        "fa-ir": "لیست تمام کیف پول(جیب تو)های موجود، نمایش داده شد. ",
    }
)

YOUR_POCKET_POCKET_NAME_LIST_ = translator(
    {
        "en-us": "A list of all available wallet(your pocket)s by pocket name is displayed.",
        "fa-ir": "لیست تمام کیف پول(جیب تو)های موجود بر اساس نام جیب، نمایش داده شد. ",
    }
)

TRANSACTION_LIST_BY_OWNER = translator(
    {
        "en-us": "A list of all the transactions made by the person you are looking for.",
        "fa-ir": "لیست تمام تراکنش هایی که شخص مورد نظر شما انجام داده است.",
    }
)

TRANSACTION_LIST_BY_YOUR_POCKET = translator(
    {
        "en-us": "A list of all transactions related to a specific wallet (your pocket) was displayed.",
        "fa-ir": "لیست تمام تراکنش های مربوط به یک کیف پول(جیب تو) مشخص نمایش داده شد.",
    }
)

TRANSACTION_LIST_BY_WALLET = translator(
    {
        "en-us": "A list of all transactions related to a specific wallet was displayed.",
        "fa-ir": "لیست تمام تراکنش های مربوط به یک کیف پول مشخص نمایش داده شد.",
    }
)

TRANSACTION_LIST_NOT_APPLIED = translator(
    {
        "en-us": "List of failed transactions displayed.",
        "fa-ir": "لیست تراکنش های ناموفق نمایش داده شد.",
    }
)

TRANSACTION_LIST_APPLIED = translator(
    {
        "en-us": "List of successful transactions displayed.",
        "fa-ir": "لیست تراکنش های موفق نمایش داده شد.",
    }
)

TRANSACTION_LIST = translator(
    {
        "en-us": "A list of all completed (successful and unsuccessful) transactions was displayed.",
        "fa-ir": " لیست تمام تراکنش های انجام شده (موفق و ناموفق) نمایش داده شد.",
    }
)

TRANSACTION_USER_LIST = translator(
    {
        "en-us": "The list of transactions of the desired user was displayed.",
        "fa-ir": "لیست تراکنش های کاربر مورد نظر نمایش داده شد.",
    }
)

REQUIRED = translator(
    {
        "fa-ir": "اجباری",
        "en-us": "required",
    }
)

OPTIONAL = translator(
    {
        "fa-ir": "اختیاری",
        "en-us": "optional",
    }
)

TRANSACTION_LOWER = translator(
    {
        "en-us": "The transaction amount is less than the allowed limit.",
        "fa-ir": "مبلغ تراکنش کمتر از حد مجاز است.",
    }
)

TRANSACTION_UPER = translator(
    {
        "en-us": "The transaction amount is more than allowed.",
        "fa-ir": "مبلغ تراکنش بیشتر از حد مجاز است.",
    }
)

WALLET_IS_BLOCK = translator(
    {
        "en-us": "The wallet is intended for the block. In this case you can not withdraw from the account.",
        "fa-ir": "کیف پول مد نظر بلاک می باشد. در این وضعیت شما نمی توانید برداشت از حساب داشته باشید.",
    }
)

YOUR_POCKET_NOT_ENOUGH = translator(
    {
        "en-us": "Wallet account balance (in your pocket) is not enough.",
        "fa-ir": "موجودی حساب کیف پول(جیب تو) کافی نمی باشد.",
    }
)

YOUR_POCKET_EXPIRED = translator(
    {
        "en-us": "Wallet (your pocket) has expired.",
        "fa-ir": "زمان اعتبار کیف پول(جیب تو) به اتمام رسیده است.",
    }
)
