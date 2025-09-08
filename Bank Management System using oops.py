{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ededb025-ef74-4605-a1b1-b9e55f0c302d",
   "metadata": {},
   "source": [
    "#### 1. Bank Management System \n",
    "\n",
    "    Concepts Used: Inheritance, abstraction, encapsulation\n",
    "    \n",
    "    Features:\n",
    "    \n",
    "    Deposit/withdraw money\n",
    "    \n",
    "    Account balance\n",
    "    \n",
    "    Savings & Current accounts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2608572c-3660-4782-a174-2830331d6c4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "class bank:\n",
    "    def __init__(self, acc_number, account_holder, balance=0.0, name='Default'):\n",
    "        self.name = name\n",
    "        self.account_holder = account_holder\n",
    "        self.acc_number = acc_number\n",
    "        self.__balance = balance   # Encapsulation\n",
    "\n",
    "    # Getters\n",
    "    def get_account_holder(self):\n",
    "        return self.account_holder\n",
    "\n",
    "    def get_account_number(self):\n",
    "        return self.acc_number\n",
    "\n",
    "    def get_balance(self):\n",
    "        return self.__balance\n",
    "\n",
    "    # Deposit\n",
    "    def deposit(self, amount):\n",
    "        if amount > 0:\n",
    "            self.__balance += amount\n",
    "            print(f\"Deposited: {amount}, New balance: {self.__balance}\")\n",
    "        else:\n",
    "            print(\"Deposit amount must be positive!\")\n",
    "\n",
    "    # Withdraw\n",
    "    def withdraw(self, amount):\n",
    "        if 0 < amount <= self.__balance:\n",
    "            self.__balance -= amount\n",
    "            print(f\"Withdrew: {amount}, New balance: {self.__balance}\")\n",
    "        else:\n",
    "            print(\"Insufficient funds or invalid amount!\")\n",
    "\n",
    "    # Protected update method\n",
    "    def _update_balance(self, new_balance):\n",
    "        self.__balance = new_balance\n",
    "\n",
    "    def result(self):\n",
    "        print(\n",
    "            f\"Account holder name: {self.account_holder} \\n\"\n",
    "            f\"Account number: {self.acc_number} \\n\"\n",
    "            f\"Type of account: {self.account_type()} \\n\"\n",
    "            f\"Balance: {self.get_balance()}\\n\")\n",
    "\n",
    "# Inheritance - Savings\n",
    "class saving_account(bank):\n",
    "    def __init__(self, acc_number, account_holder, balance=0.0):\n",
    "        super().__init__(acc_number, account_holder, balance)\n",
    "\n",
    "    def account_type(self):\n",
    "        return \"Saving Account\"\n",
    "\n",
    "\n",
    "# Inheritance - Current\n",
    "class current_account(bank):\n",
    "    def __init__(self, acc_number, account_holder, balance=0.0, overdraft_amount=1000):\n",
    "        super().__init__(acc_number, account_holder, balance)\n",
    "        self.overdraft_amount = overdraft_amount\n",
    "\n",
    "    # Overriding withdraw\n",
    "    def withdraw(self, amount):\n",
    "        if amount > 0 and (self.get_balance() + self.overdraft_amount) >= amount:\n",
    "            new_balance = self.get_balance() - amount\n",
    "            self._update_balance(new_balance)\n",
    "            print(f\"Withdrew: {amount}. Remaining Balance: {self.get_balance()}\")\n",
    "        else:\n",
    "            print(\"Withdrawal exceeds overdraft limit or invalid amount!\")\n",
    "\n",
    "    def result(self):\n",
    "        \n",
    "        return (\n",
    "             f\"Account holder name: {self.account_holder} \\n \"\n",
    "             f\"Account number: {self.acc_number}\\n \"\n",
    "             f\"Type of account: {self.account_type()} \\n\"\n",
    "             f\"Balance: {self.get_balance()}\" )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "0ef866e6-ebe5-4ec8-b97a-346e29772dea",
   "metadata": {},
   "outputs": [],
   "source": [
    "acc1 = saving_account(12, \"umang\", 5000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "475cca35-2361-49da-af2d-f0197eb0befd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Saving Account'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "acc1.account_type()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "40cd5ee8-0d0e-4e22-ac24-d31420ab0943",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Deposited: 1000, New balance: 6000\n"
     ]
    }
   ],
   "source": [
    "acc1.deposit(1000)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6c821d5c-a638-4659-90cc-512a10f73d27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Withdrew: 500, New balance: 5500\n"
     ]
    }
   ],
   "source": [
    "acc1.withdraw(500)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "1cb6ebb3-6009-463a-a255-b6090bc65294",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Account holder name: umang \n",
      "Account number: 12 \n",
      "Type of account: Saving Account \n",
      "Balance: 5500\n",
      "\n"
     ]
    }
   ],
   "source": [
    "acc1.result()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "202e67f0-2904-4f6c-be3b-7f4deb2a7a35",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "12"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "acc1.get_account_number()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "965c4d90-523c-49d5-84c1-401372c42a24",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d7efd12-e54c-4ef8-a5b2-6e0f461a4ef3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7a9b1b5c-7eba-4da1-8627-6519f5d73fc6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  },
  "widgets": {
   "application/vnd.jupyter.widget-state+json": {
    "state": {},
    "version_major": 2,
    "version_minor": 0
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
