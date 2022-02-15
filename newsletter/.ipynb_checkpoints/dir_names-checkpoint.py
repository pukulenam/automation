{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "0b902a78-7f2f-4618-8c3e-63958bcaa24d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030, 2031, 2032,\n",
       "       2033, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043,\n",
       "       2044, 2045, 2046, 2047, 2048, 2049, 2050])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "years = np.arange(2022, 2051, dtype=int)\n",
    "years"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "eae27461-4566-4b63-8cac-895a2fa7f361",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['January',\n",
       " 'February',\n",
       " 'March',\n",
       " 'April',\n",
       " 'May',\n",
       " 'June',\n",
       " 'July',\n",
       " 'August',\n",
       " 'September',\n",
       " 'October',\n",
       " 'November',\n",
       " 'December']"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import calendar\n",
    "months = [x for x in calendar.month_name if x] \n",
    "months"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0b4f0946-e84e-4c9b-9d67-0bad55768c5f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,\n",
       "       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30])"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "days1 = np.arange(1, 31, dtype=int)\n",
    "days1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "b20d5639-9b8e-42f9-8a2a-b4076e4a907b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,\n",
       "       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "days2 = np.arange(1, 32, dtype=int)\n",
    "days2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "6ea10200-74e7-4930-90ac-60039bfe5eee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,\n",
       "       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29])"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "daysNoLeap = np.arange(1, 30, dtype=int)\n",
    "daysNoLeap"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "73ba876a-74c6-4f11-b226-06c842e2aed2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([ 1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,\n",
       "       18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "daysLeap = np.arange(1, 29, dtype=int)\n",
    "daysLeap"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b0fb1ba-e1fa-41ad-8cf0-8660d9605156",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
