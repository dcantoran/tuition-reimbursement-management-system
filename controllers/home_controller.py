# For any request not pointing to a specific model
import psycopg2
import psycopg2.extras
from flask import Flask, session, render_template, request, redirect, g, url_for, flash
from util.db_connection import connection
from services.form_service import FormService
from repositories.form_repo import FormRepo

fr = FormRepo()
fs: FormService = FormService(fr)


def route(app):
    @app.route('/', methods=['GET', 'POST'])
    def index():
        cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            # session.pop('user', None)
            name = request.form['username']
            a_id = request.form['password']

            cur.execute('SELECT * FROM applicant WHERE name = %s AND a_id = %s', (name, a_id,))
            applicant = cur.fetchone()
            # print(applicant)

            if applicant:
                session['loggedIn'] = True
                session['id'] = applicant['a_id']
                session['user'] = applicant['name']
                return redirect(url_for('protected'))

            # From 12 min video
            # if request.form['password'] == 'password':
            #     session['user'] = request.form['username']
            #     return redirect(url_for('protected'))

        return render_template('index.html')

    @app.route('/protected/', methods=['GET', 'POST'])
    def protected():
        cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if request.method == 'POST' and 'username' in request.form and 'appId' in request.form:
            # session.pop('user', None)
            a_name = request.form['username']
            location = request.form['location']
            description = request.form['description']
            e_cost = request.form['eCost']
            e_type = request.form['eType']
            grade_format = request.form['gradeFormat']
            app_id = request.form['appId']
            cur.execute('INSERT INTO form (a_name, location, description, e_cost, e_type, grade_format, app_id) VALUES '
                        '(%s, %s, %s, %s, %s, %s, %s)',
                        (a_name, location, description, e_cost, e_type, grade_format, app_id))
            connection.commit()
            flash('Successfully Added Form!')

        if g.user:
            # print(g.user)
            return render_template('protected.html', user=session['user'], id=session['id'])
        return redirect(url_for('index'))

    @app.before_request
    def before_request():
        g.user = None

        if 'user' in session:
            g.user = session['user']

    @app.route('/dropsession/')
    def dropsession():
        session.pop('user', None)
        return render_template('index.html')

    @app.route('/applications/', methods=['GET', 'POST'])
    def applications():
        cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if 'loggedIn' in session:
            # cur.execute('SELECT * FROM form WHERE app_id = %s', [session['id']])
            # account = cur.fetchall()
            # a_name = account[1]
            # print(account)
            account = fs.get_all_forms_by_applicant_id(session['id'])
            print(account)
            return render_template('applications.html', account=account, user=session['user'])
        return redirect(url_for('login'))

    @app.route('/bc_login/', methods=['GET', 'POST'])
    def bc_login():
        cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            name = request.form['username']
            bc_id = request.form['password']

            cur.execute('SELECT * FROM benco WHERE name = %s AND bc_id = %s', (name, bc_id))
            benco = cur.fetchone()

            if benco:
                session['loggedIn'] = True
                session['id'] = benco['bc_id']
                session['user'] = benco['name']
                return redirect(url_for('bc_protected'))
        if g.user:
            # print(g.user)
            return render_template('/bc_templates/bc_protected.html', user=session['user'], id=session['id'])
        return render_template('/bc_templates/bc_login.html')
        # return render_template('bc_login.html')

    @app.route('/bc_protected/')
    def bc_protected():
        if g.user:
            # print(g.user)
            return render_template('/bc_templates/bc_protected.html', user=session['user'], id=session['id'])
        return render_template('/bc_templates/bc_login.html')

    @app.route('/bc_applications/', methods=['GET', 'POST'])
    def bc_applications():
        cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if 'loggedIn' in session:
            # cur.execute('SELECT * FROM form WHERE app_id = %s', [session['id']])
            # account = cur.fetchall()
            # a_name = account[1]
            # print(account)
            benco_account = fs.get_all_forms_by_applicant_benco_id(session['id'])
            print(benco_account)
            return render_template('/bc_templates/bc_applications.html',
                                   benco_account=benco_account, user=session['user'])
        return redirect(url_for('bc_login'))

    @app.route('/dh_login/', methods=['GET', 'POST'])
    def dh_login():
        cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            name = request.form['username']
            dh_id = request.form['password']

            cur.execute('SELECT * FROM dept_head WHERE name = %s AND dh_id = %s', (name, dh_id))
            dept_head = cur.fetchone()

            if dept_head:
                session['loggedIn'] = True
                session['id'] = dept_head['dh_id']
                session['user'] = dept_head['name']
                return redirect(url_for('dh_protected'))
        if g.user:
            # print(g.user)
            return render_template('/dh_templates/dh_protected.html', user=session['user'], id=session['id'])
        return render_template('/dh_templates/dh_login.html')
        # return render_template('bc_login.html')

    @app.route('/dh_protected/')
    def dh_protected():
        if g.user:
            # print(g.user)
            return render_template('/dh_templates/dh_protected.html', user=session['user'], id=session['id'])
        return render_template('/dh_templates/dh_login.html')

    @app.route('/dh_applications/', methods=['GET', 'POST'])
    def dh_applications():
        cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if 'loggedIn' in session:
            # cur.execute('SELECT * FROM form WHERE app_id = %s', [session['id']])
            # account = cur.fetchall()
            # a_name = account[1]
            # print(account)
            dept_head = fs.get_all_forms_by_applicant_depthead_id(session['id'])
            print(dept_head)
            return render_template('/dh_templates/dh_applications.html',
                                   dept_head=dept_head, user=session['user'])
        return redirect(url_for('dh_login'))

    @app.route('/sv_login/', methods=['GET', 'POST'])
    def sv_login():
        cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
            name = request.form['username']
            sv_id = request.form['password']

            cur.execute('SELECT * FROM supervisor WHERE name = %s AND sv_id = %s', (name, sv_id))
            supervisor = cur.fetchone()

            if supervisor:
                session['loggedIn'] = True
                session['id'] = supervisor['sv_id']
                session['user'] = supervisor['name']
                return redirect(url_for('sv_protected'))
        if g.user:
            # print(g.user)
            return render_template('/sv_templates/sv_protected.html', user=session['user'], id=session['id'])
        return render_template('/sv_templates/sv_login.html')
        # return render_template('bc_login.html')

    @app.route('/sv_protected/')
    def sv_protected():
        if g.user:
            # print(g.user)
            return render_template('/sv_templates/sv_protected.html', user=session['user'], id=session['id'])
        return render_template('/sv_templates/sv_login.html')

    @app.route('/sv_applications/', methods=['GET', 'POST'])
    def sv_applications():
        cur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if 'loggedIn' in session:
            # cur.execute('SELECT * FROM form WHERE app_id = %s', [session['id']])
            # account = cur.fetchall()
            # a_name = account[1]
            # print(account)
            sv_account = fs.get_all_forms_by_applicant_super_id(session['id'])
            print(sv_account)
            return render_template('/sv_templates/sv_applications.html',
                                   sv_account=sv_account, user=session['user'])
        return redirect(url_for('sv_login'))


# if __name__ == '__main__':






