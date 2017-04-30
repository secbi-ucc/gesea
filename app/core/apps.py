from suit.apps import DjangoSuitConfig
from suit.menu import ParentItem, ChildItem

class SuitConfig(DjangoSuitConfig):
    name = 'suit'
    verbose_name = 'Django Suit'
    # Menu and header layout - horizontal or vertical
    layout = 'horizontal'

    # Set default list per page
    list_per_page = 20

    # Show changelist top actions only if any row is selected
    toggle_changelist_top_actions = True

    # Define menu
    #: :type: list of suit.menu.ParentItem
    menu = (
        ParentItem('Listados', children=[
            ChildItem(model='inscripcion.estudiantes'),
            ChildItem(model='inscripcion.programa'),
            ChildItem(model='inscripcion.instructor'),

            # ChildItem('Custom view', url='/admin/custom/'),
        ]),
        ParentItem('Actividades', children=[
            ChildItem(model='actividades.actividad'),
            ChildItem(model='actividades.area'),

        ]),
        ParentItem('Programacion', children=[
            ChildItem(model='programacion.horario'),
            ChildItem(model='programacion.diaactividad'),
            ChildItem(model='programacion.lugar'),
        ]),
        ParentItem('Inscripciones', children=[
            ChildItem(model='inscripcion.inscripcion'),
            ChildItem(model='programacion.programacion'),
            # ChildItem('Custom view', url='/admin/custom/'),
        ]),
        ParentItem('Asistencia', children=[
            ChildItem('Tomar asistencia', url='/admin/asistencia/'),
            ChildItem('Mi lista ', url='/admin/asistencia/1'),
            ChildItem(model='inscripcion.asistenciaestudiante'),
        ]),
        ParentItem('Usuarios', children=[
            ChildItem(model='auth.user'),
            ChildItem(model='auth.group'),

        ]),

    )