from tonsdk.contract.wallet import Wallets, WalletVersionEnum


mnemonics = ['earn', 'dust', 'piano', 'thing', 'task', 'fabric', 'list', 'hip', 'multiply', 'member', 'race', 'session', 'embody', 'biology', 'piano', 'desert', 'practice', 'glimpse', 'organ', 'roof', 'critic', 'lottery', 'viable', 'film']


mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2, workchain=0)

wallet_address = wallet.address.to_string(True, True, True)

if __name__ == '__main__':
    print(wallet_address)  # kQB_bTCXmQpIldjAj5tGKKKl6p7JD-jDF0YQqmoyxffjg4sD
