# -*- coding: utf-8 -*-
{
    'name': "agent_functionality",

    'summary': """
        Adds agent functionality
        """,

    'description': """
        8. Розширити базового партнерана поняттям Агента. В картці партнера є 
        можливість вказати що він є агентом, далі зявляється окрема вкладка з 
        налаштуваннями там потрібно вказати продукт (доступні тільки 
        послуги), %. В замовленні продаж є можливість обрати обрати агента 
        на кожен окремий продукт, при підтвердженні замовлення створювати 
        рахунок на продукт що вказаний в картці, вартість розраховується з 
        маржі продажу (ціна продажу - собівартість * кількість) * % агента. 
        При відмінні замовлення відміняти і рахунок, якщо рахунок оплачений 
        вивести повідомлення. 
    """,

    'author': "Igor Kurilko",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'crm',
        'sale',
        'product',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/res_partner.xml',
        'views/sale_order.xml',
    ],
}