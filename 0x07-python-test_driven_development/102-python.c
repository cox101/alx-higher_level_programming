#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_string(PyObject *p);

int main(int argc, char *argv[]) {
    Py_Initialize();
    PyObject *str = PyUnicode_DecodeUTF8("Hello, Python!", 13, "strict");
    print_python_string(str);
    Py_DECREF(str);
    Py_Finalize();
    return 0;
}

void print_python_string(PyObject *p) {
    // Check if the object is a valid string
    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "Invalid String Object\n");
        return;
    }

    Py_ssize_t size;
    const char *str = PyUnicode_AsUTF8AndSize(p, &size);

    printf("  [.] string object info\n");
    printf("    type: %s\n", Py_TYPE(p)->tp_name);
    printf("    length: %zd\n", size);
    printf("    value: %s\n", str);
}

