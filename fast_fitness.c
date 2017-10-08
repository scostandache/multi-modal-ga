#include <Python.h>
#include <stdio.h>

static PyObject *rastrigin(PyObject *self, PyObject *args);
static PyObject *rosenbrock(PyObject *self, PyObject *args);
static PyObject *griewangk(PyObject *self, PyObject *args);
static PyObject *SHCB(PyObject *self, PyObject *args);

static PyMethodDef FitnessMethods[]={
	{"rastrigin", rastrigin, METH_VARARGS},
	{"rosenbrock", rosenbrock, METH_VARARGS},
	{"griewangk", griewangk, METH_VARARGS},
	{"SHCB", SHCB, METH_VARARGS},
	{NULL, NULL}
}

void initfast_fitness(){
	(void)Py_InitModule("fast_fitness", FitnessMethods);
}