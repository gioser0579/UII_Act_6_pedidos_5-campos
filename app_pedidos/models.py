from django.db import models

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.IntegerField()  # Asumiendo que id_cliente se referirá a un cliente existente
    fecha_entrega = models.DateField()
    fecha_pedido = models.DateField()
    estado = models.CharField(max_length=100)
    total = models.IntegerField()

    def __str__(self):
        return f"Pedido {self.id_pedido} - Cliente {self.id_cliente}"
