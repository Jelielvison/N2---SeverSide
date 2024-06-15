import gerador
import merge_sort
from app import app, db, ValueModel
from sqlalchemy import text


# Gerar lista ordenada
vetor_ordenado = gerador.gerar_vetor()
print(vetor_ordenado)

# Randomizar vetor
vetor_randomizado = gerador.randomizar_vetor(vetor_ordenado)
print(vetor_randomizado)

# Aplicar o merge sort na lista randomizada
vetor_reordenado = merge_sort.merge_sort(vetor_randomizado)
print(vetor_reordenado)

def insert_values_in_batches(vetor_randomizado, batch_size=50000):
    for i in range(0, len(vetor_randomizado), batch_size):
        batch = vetor_randomizado[i:i+batch_size]
        vetor = [ValueModel(value=value) for value in batch]
        with app.app_context():
            db.session.execute(text('TRUNCATE TABLE value_model'))
            db.session.bulk_save_objects(vetor)
            db.session.commit()
    print("Valores inseridos com sucesso!")

if __name__ == '__main__':
    insert_values_in_batches(vetor_randomizado)

