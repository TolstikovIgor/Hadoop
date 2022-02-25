## Урок 6. ETL
#### Домашнее задание
Sqoop:
1. Получаем список таблиц, которые созданы в postgres (нужно правильно указать ip, сейчас указан localhost)

```sqoop list-tables --connect jdbc:postgresql://localhost/pg_db --username exporter --password exporter_pass```

2. Запускаем импорт:

```sqoop import --connect jdbc:postgresql://10.0.0.7/lesson5 --username exporter
--password exporter_pass --table character --hive-import --hive-database lesson6_9
--hive-table character
```

Flume:
1. Запускаем flume (нужно правильно указать пути до папки и файла)

```/opt/apache-flume/bin/flume-ng agent --conf /home/admin/flm/ --conf-file
 /home/admin/flm/flm.conf --name StudentFlume -Dflume.root.logger=INFO,console
 ```

2. Создаем таблицы в hive

```
create external table lesson10_6.flm_logs (first string, second string, third string, fourth string, fifth string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS INPUTFORMAT 'org.apache.hadoop.mapred.SequenceFileInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io.HiveSequenceFileOutputFormat'
location '/user/centos/flm'
```
