#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");
    if (PyList_Check(p)) {
        size = PyList_Size(p);
        printf("[*] Size of the Python List: %ld\n", size);
        printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

        for (i = 0; i < size; i++) {
            item = PyList_GetItem(p, i);
            printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        }
    } else {
        printf("  [ERROR] Invalid List Object\n");
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *bytes;

    printf("[.] Bytes object info\n");
    if (PyBytes_Check(p)) {
        size = PyBytes_Size(p);
        printf("[*] Size of the Python Bytes: %ld\n", size);
        bytes = PyBytes_AsString(p);

        printf("[.1] First %ld bytes: ", size + 1 > 10 ? 10 : size + 1);
        for (i = 0; i < size + 1 && i < 10; i++) {
            printf("%02x ", (unsigned char)bytes[i]);
        }
        printf("\n");
    } else {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}

void print_python_float(PyObject *p) {
    printf("[.] Float object info\n");
    if (PyFloat_Check(p)) {
        printf("[*] Value: %f\n", ((PyFloatObject *)p)->ob_fval);
    } else {
        printf("  [ERROR] Invalid Float Object\n");
    }
}

