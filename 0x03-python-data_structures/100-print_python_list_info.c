#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p) {
    PyListObject *list;
    Py_ssize_t size, alloc, i;

    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid Python list\n");
        return;
    }

    list = (PyListObject *)p;
    size = PyList_Size(p);
    alloc = list->allocated;

    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", alloc);

    for (i = 0; i < size; i++) {
        printf("Element %zd: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
    }
}

