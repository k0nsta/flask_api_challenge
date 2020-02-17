from src.managers.subsriptions import SubscriptionManager


def check_subscription_data_limit(sid):
    SubscriptionManager.set_service_block_code(sid)


def check_all_subscription_data_limit():
    sids = SubscriptionManager.get_all_ids()
    for i in sids:
        check_subscription_data_limit(i)

