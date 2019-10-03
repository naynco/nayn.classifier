from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def suggest():
    data = request.json
    return jsonify(data)

@app.route('/api/v1/tag', methods=['POST'])
def suggest():
    data = request.json
    return jsonify(data)


@app.route('/api/v1/version', methods=['POST'])
def getWPVersion(install_root_dir):
    """Retrieves Wordpress current version and return it as a string
    
    Args:
        install_root_dir (str): Path to public root direcotry for WP installation.
    Returns:
        version (str): WP version retrived by WP CLI, False if exception is raised
    """
    try:
        version = check_output(['wp', '--path='+install_root_dir, 'core', 'version'])
    except:
        print('Oooops seems like WP-CLI is not working properly in your Wordpress installation')
        return  False
    return jsonify(version.decode('utf-8')[0:5])
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')