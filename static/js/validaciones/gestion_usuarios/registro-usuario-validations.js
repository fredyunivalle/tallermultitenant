form = "#usuario-form";
fields = {
    first_name: {
        validators: {
            notEmpty: {
                message: MENSAJE_VACIO
            }
        }
    },
    last_name: {
        validators: {
            notEmpty: {
                message: MENSAJE_VACIO
            }
        }
    },
    username: {
        validators: {
            notEmpty: {
                message: MENSAJE_VACIO
            }
        }
    },
    password: {
        validators: {
            notEmpty: {
                message: MENSAJE_VACIO
            }
        }
    },
    confirmar_pass: {
        validators: {
            notEmpty: {
                message: MENSAJE_VACIO
            },
            identical: {
                field: 'password',
                message: 'La contraseña no es igual a la de confirmación'
            }
        }
    },
    tipo_id: {
        validators: {
            notEmpty: {
                message: MENSAJE_VACIO
            }
        }
    },
    identificacion: {
        validators: {
            notEmpty: {
                message: MENSAJE_VACIO
            }
        }
    },
    fecha_nacimiento: {
        validators: {
            notEmpty: {
                message: MENSAJE_VACIO
            },
            date: {
                message: 'El valor ingresado no es una fecha válida, debe ser menor a la fecha actual',
                format: 'YYYY-MM-DD',
                max: function(field, validator){
                    var d = new Date();

                    var curr_date = d.getDate();

                    var curr_month = d.getMonth() + 1;

                    var curr_year = d.getFullYear();
                    return curr_year + "-" + curr_month + "-" + curr_date;

                }
            }
        }
    },
    email: {
        validators: {
            notEmpty: {
                message: MENSAJE_VACIO
            },
            emailAddress: {
                message: MENSAJE_CORREO
            }
        }
    },
    foto: {
        validators: {
            file: {
                message: "Por favor seleccione un archivo de imagen jpg, jpeg, png, valido",
                extension: "jpg,png,jpeg",
                type: "image/jpeg,image/png"
            }
        }
    }
};



//Revalidar campos al ser actualizados
$("#id_fecha_nacimiento").on('change',function(e){
    $("#usuario-form").bootstrapValidator('revalidateField', 'fecha_nacimiento');
});

$.getScript(base+"js/validaciones/validations-base.js");