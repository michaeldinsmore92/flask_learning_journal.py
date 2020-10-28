from flask import (Flask, g, render_template, flash,
                   redirect, url_for, request, abort)

import datetime
import forms
import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = '56dfg1dfg1vdf5v1df5vdf15v1dsfvf631b3sg84b8899bfg156sdf'


@app.before_request
def before_request():
    """Connect to the database before each request"""
    g.db = models.DATABASE
    g.db.connect()
    
    
@app.after_request
def after_request(response):
    """Close the database connection after each request"""
    g.db.close()
    return response
    
           
@app.route('/')
@app.route('/entries')
def index():
    """Main Page"""
    entries = models.Entry.select().limit(5)
    return render_template('index.html', entries=entries)
    

@app.route('/entries/new', methods=['GET', 'POST'])
def new_entry():
    """New Entry"""
    form = forms.EntryForm()
    if form.validate_on_submit():
        models.Entry.create_entry(
            title = form.title.data.strip(),
            date = form.date,
            time_spent = form.time_spent.data.strip(),
            what_you_learned = form.what_you_learned.data.strip(),
            resources_to_remember = form.resources_to_remember.data.strip(),
            tags = form.tags.data.strip()
        )
        flash("Entry posted! Thank you!", "success")
        return redirect(url_for('index'))
    return render_template('new.html', form=form)


@app.route('/entries/<id>')
def detail(id):
    """View Entry"""
    try:
        entry = models.Entry.get(models.Entry.entry_id == id)
    except models.DoesNotExist:
        abort(404)
    return render_template('detail.html', entry=entry)


@app.route('/entries/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    """Edit Entry"""
    form = forms.EntryForm()
    try:
        entry = models.Entry.get(models.Entry.entry_id == id)
    except models.DoesNotExist:
        abort(404)      
    if form.validate_on_submit():
        entry.title = form.title.data.strip()
        entry.date = form.date
        entry.time_spent = form.time_spent.data.strip()
        entry.what_you_learned = form.what_you_learned.data.strip()
        entry.resources_to_remember = form.resources_to_remember.data.strip()
        entry.tags = form.tags.data
        entry.save()
        flash("Entry saved! Thank you!", "success")
        return redirect(url_for('index'))
    else:
        return render_template('edit.html', entry=entry, form=form)    


@app.route('/entries/<id>/delete')
def delete(id):
    """Delete Entry"""
    try:
        entry = models.Entry.get(models.Entry.entry_id == id)
        entry.delete_instance()
    except models.DoesNotExist:
        abort(404)
    return redirect(url_for('index'))


@app.errorhandler(404)
def error(error):
	return render_template('404.html'), 404   


# Dunder Main        
if __name__ == '__main__':
    models.initialize()
    try:
        if models.Entry.select().where(models.Entry.title == 'First Entry').exists():
            pass
        else:
            models.Entry.create_entry(
                    title='First Entry',
                    date=datetime.datetime.now,
                    time_spent='1 Hour',
                    what_you_learned='how to cook burgers',
                    resources_to_remember='youtube',
                    tags='cooking',
                )
    except ValueError:
        pass
    
    app.run(debug=DEBUG, host=HOST, port=PORT)
    