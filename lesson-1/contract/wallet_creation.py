from tonsdk.contract.wallet import Wallets, WalletVersionEnum

mnemonics = ['earn', 'dust', 'piano', 'thing', 'task', 'fabric', 'list', 'hip', 'multiply', 'member', 'race', 'session', 'embody', 'biology', 'piano', 'desert', 'practice', 'glimpse', 'organ', 'roof', 'critic', 'lottery', 'viable', 'film']
mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2, workchain=0)

#EQCJWf81ynPtMYMaJB0V9mfopRAkMTY1yN4liFHTbBdrYPJK

#mnemonics, pub_k, priv_k, wallet = Wallets.create(version=WalletVersionEnum.v3r2, workchain=0)
    #.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v3r2, workchain=0)

#wallet_address = wallet.address.to_string(True, True, True, True)
wallet_address = wallet.address.to_string(True, True, True)

if __name__ == '__main__':
    print(mnemonics)
    #print(wallet.address.to_string(True, True, True, True))
    print(wallet.address.to_string(True, True, True))
    #print(wallet.address.to_string())
