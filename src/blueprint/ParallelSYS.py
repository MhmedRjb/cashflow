from flask import Blueprint,render_template 

ParallelSYS_bp=Blueprint('ParallelSYS',__name__)
class ParallelSYS():
    @ParallelSYS_bp.route('/Elfateh/main/Inventory/')
    def inventory():
        return render_template('inventorySYS.html')
    
    @ParallelSYS_bp.route('/Elfateh/main/reports/clinets_statistics')
    def clinets_statistics():
        return render_template('inventorySYS.html')
    
    @ParallelSYS_bp.route('/Elfateh/main/reports/genral_statistics')
    def genral_statistics():
        return render_template('inventorySYS.html')
