import bpy

class ModalMoveOperator2D(bpy.types.Operator):
    """Movimiento 2D real: Flechas para X y Z"""
    bl_idname = "object.modal_move_operator_2d"
    bl_label = "Modal Move Operator 2D"

    def modal(self, context, event):
        obj = bpy.data.objects.get("Stroke")
        
        if obj is None:
            return {'FINISHED'}

        if event.value == 'PRESS':
            # --- MOVIMIENTO HORIZONTAL ---
            if event.type == 'LEFT_ARROW':
                obj.location.x -= 0.5
            elif event.type == 'RIGHT_ARROW':
                obj.location.x += 0.5
            
            # --- MOVIMIENTO VERTICAL (CORREGIDO) ---
            # Usamos 'z' para que suba/baje en la pantalla 
            # y no se acerque/aleje (que es lo que hace el eje 'y')
            elif event.type == 'UP_ARROW':
                obj.location.z += 0.5
            elif event.type == 'DOWN_ARROW':
                obj.location.z -= 0.5

            # Salida del modo
            elif event.type == 'ESC':
                print("Control 2D finalizado.")
                return {'FINISHED'}

        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        context.window_manager.modal_handler_add(self)
        print("Control 2D Activo: Flechas para mover, ESC para salir.")
        return {'RUNNING_MODAL'}

# Registro del operador
if hasattr(bpy.types, "ModalMoveOperator2D"):
    bpy.utils.unregister_class(ModalMoveOperator2D)
    
bpy.utils.register_class(ModalMoveOperator2D)
bpy.ops.object.modal_move_operator_2d('INVOKE_DEFAULT')
