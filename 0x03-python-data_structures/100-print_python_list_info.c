#include <stdio.h>
#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to python list
 */
void print_python_list_info(PyObject *p)
{
	int j = 0, listLen = 0;
	PyObject *item;
	PyListObject *clone = (PyListObject *) p;

	listLen = Py_SIZE(p);
	printf("[*] Size of the Python List = %d\n", listLen);
	printf("[*] Allocated = %d\n", (int) clone->allocated);

	for (; j < listLen; ++j)
	{
		item = PyList_GET_ITEM(p, j);
		printf("Element %d: %s\n", j, item->ob_type->tp_name);
	}
}
