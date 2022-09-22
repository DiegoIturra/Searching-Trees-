FECHA=$(date +"%Y-%m-%d-%H-%M-%S")

for i in {500..10000..500}
do
    python3 mainOrdenado.py $i >> ordenado_$FECHA.txt
done

for i in {5000..100000..5000}
do
    python3 mainDesordenado.py $i >> desordenado_$FECHA.txt
done