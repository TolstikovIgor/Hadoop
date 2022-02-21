1. Запустить задачу из примеров, например, вычисление pi методом Монте-Карло
yarn jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-mapreduce-examples.jar pi 32 10000
зайти на ResourceManager http://manager.novalocal:8088 и найти свою задачу.
2. Запустить WordCount и доработать скрипт из примера, чтобы удалялись знаки препинания и слова считались в нижнем регистре.
3.   Написать MapReduce для своего датасета, который бы реализовывал аналитическую операцию
