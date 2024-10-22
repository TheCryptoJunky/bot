# main.py
import logging
import config
import goal_manager
import learning_agent
import wallet
import wallet_manager
import wallet_swarm
import trade
import gui

def main():
    config = config.Config()
    goal_manager = goal_manager.GoalManager(config)
    learning_agent = learning_agent.LearningAgent(config, goal_manager)
    wallet = wallet.Wallet(config)
    wallet_manager = wallet_manager.WalletManager(config)
    wallet_swarm = wallet_swarm.WalletSwarm(config)
    trade = trade.Trade(config, wallet)
    gui = gui.GUI(config)

    # Start the GUI
    gui.run()

if __name__ == '__main__':
    main()
