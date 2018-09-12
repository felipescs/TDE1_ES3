import pytest
from app import soma
from app import subtra
from app import mult

def test_soma1():
	assert soma(1,1)==2
	assert soma(-1,-2)==-3
	assert soma(-1,3)==2
	assert soma(1.2,2.3)==3.5
	assert soma(2,2)==4
	assert soma('2',2)==4
def test_subtra1():
	assert subtra(1,1)==0
	assert subtra(3.2,2.2)==1

def test_mult():
	assert mult(1,2)==2
