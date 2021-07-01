{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "30\n"
     ]
    }
   ],
   "source": [
    "a = 10\n",
    "b = 20\n",
    "print(a+b)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 기본 함수 연습 01\n",
    "<h1> 기본 연습 </h1>\n",
    "<h2> 기본 연습 </h2>\n",
    "<h3> 기본 연습 </h3>\n",
    "<h4> 기본 연습 </h4>\n",
    "<h5> 기본 연습 </h5>\n",
    "HTML : Hyper Text Markup Language\n",
    "                        <,>,/"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def add(a,b):\n",
    "    return a+b\n",
    "\n",
    "a = 3\n",
    "b = 4\n",
    "c = add(a,b) #3,4는 인수\n",
    "\n",
    "print(\"%d+%d=%d\"%(a,b,c))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5+3=8\n",
      "--------------------\n"
     ]
    }
   ],
   "source": [
    "# 매개변수 지정하여 호출하기\n",
    "#1.일반적인 함수\n",
    "\n",
    "def add(a,b): #a,b 는 매개변수\n",
    "    return a, b, a+b\n",
    "\n",
    "a,b,result=add(b=5,a=3)\n",
    "print(\"%d+%d=%d\"%(b,a,result))\n",
    "print(\"-\"*20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi\n",
      "--------------------\n"
     ]
    }
   ],
   "source": [
    "#2.입력값이 없는 함수\n",
    "def say():\n",
    "    return 'Hi'\n",
    "\n",
    "print(say())\n",
    "print(\"-\"*20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3,4의 합은 7 입니다.\n",
      "None\n",
      "--------------------\n"
     ]
    }
   ],
   "source": [
    "#3. 결괏값이 없는 함수\n",
    "#결괏값은 오직 return 명령어로만 돌려받을 수 있다.\n",
    "\n",
    "def add2(a,b):\n",
    "    print(\"%d,%d의 합은 %d 입니다.\"%(a,b,a+b))\n",
    "    \n",
    "print(add2(3,4))\n",
    "print(\"-\"*20)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi\n",
      "--------------------\n"
     ]
    }
   ],
   "source": [
    "#4. 입력값도 결괏값도 없는 함수\n",
    "\n",
    "def say2():\n",
    "    print('Hi')\n",
    "    \n",
    "say2()\n",
    "print(\"-\"*20)"
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
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
