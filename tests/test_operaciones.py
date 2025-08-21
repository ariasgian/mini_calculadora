import src.calculos2.operaciones as op
def test_suma():
    assert(op.sumar(5,3))==8
def test_resta():
    assert(op.restar(8,5))==3
def test_multiplicar():
    assert op.multiplicar(5,8)==40
def test_dividir():
    assert op.dividir(15,5)==3
    assert op.dividir(15,0)=='no puede generar la operacion porque b =0'