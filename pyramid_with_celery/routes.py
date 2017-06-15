def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('task1', '/task1')
    config.add_route('task1_result', '/task1_result/{task_id}')
