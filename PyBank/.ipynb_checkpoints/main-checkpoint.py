{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#import dictionaries\n",
    "\n",
    "import pandas as pd\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10-Jan</td>\n",
       "      <td>867884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10-Feb</td>\n",
       "      <td>984655</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10-Mar</td>\n",
       "      <td>322013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10-Apr</td>\n",
       "      <td>-69417</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>10-May</td>\n",
       "      <td>310503</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Date  Profit/Losses\n",
       "0  10-Jan         867884\n",
       "1  10-Feb         984655\n",
       "2  10-Mar         322013\n",
       "3  10-Apr         -69417\n",
       "4  10-May         310503"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#open and read first 5 rows of the csv\n",
    "\n",
    "pybank_path=\"PyBank.csv\"\n",
    "pybank_df=pd.read_csv(pybank_path)\n",
    "pybank_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "      <th>Profit Change</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10-Jan</td>\n",
       "      <td>867884</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10-Feb</td>\n",
       "      <td>984655</td>\n",
       "      <td>116771.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10-Mar</td>\n",
       "      <td>322013</td>\n",
       "      <td>-662642.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>10-Apr</td>\n",
       "      <td>-69417</td>\n",
       "      <td>-391430.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>10-May</td>\n",
       "      <td>310503</td>\n",
       "      <td>379920.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Date  Profit/Losses  Profit Change\n",
       "0  10-Jan         867884            NaN\n",
       "1  10-Feb         984655       116771.0\n",
       "2  10-Mar         322013      -662642.0\n",
       "3  10-Apr         -69417      -391430.0\n",
       "4  10-May         310503       379920.0"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Using the dif function to calculate changes from previous month\n",
    "\n",
    "profit_dif_test=pybank_df['Profit/Losses'].diff()\n",
    "pybank_df['Profit Change'] = profit_dif_test\n",
    "\n",
    "pybank_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Financial Analysis\n",
      "------------------------------\n",
      "Total Months: 86\n",
      "Total: $38382578\n",
      "Average Monthly Change: $-2315.1176470588234\n",
      "Largest Increase: $1926159.0 occurred during 12-Feb\n",
      "Largest Decrease: $-2196167.0 occurred during 13-Sep\n"
     ]
    }
   ],
   "source": [
    "#printing outputs\n",
    "\n",
    "print(\"\")\n",
    "print(\"Financial Analysis\")\n",
    "print(\"------------------------------\")\n",
    "print(\"Total Months: \" + str(pybank_df.shape[0]))\n",
    "print(\"Total: $\" + str(pybank_df['Profit/Losses'].sum()))\n",
    "print(\"Average Monthly Change: $\" + str(pybank_df['Profit Change'].mean()))\n",
    "print(\"Greatest Increase in Profits: $\" + str(pybank_df['Profit Change'].max()) + \" occurred during \" + pybank_df.loc[pybank_df['Profit Change'].idxmax(), 'Date'])\n",
    "print(\"Greatest Decrease in Profits: $\" + str(pybank_df['Profit Change'].min()) + \" occurred during \" + pybank_df.loc[pybank_df['Profit Change'].idxmin(), 'Date'])"
   ]
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
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
