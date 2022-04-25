from flask import Flask, render_template, request
import onnx
import onnxruntime as rt
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/return_file', methods=['POST'])
def return_file():
    # https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
    onnx_file = request.files['file']
    onnx_file_name = onnx_file.filename
    onnx_file_stream = onnx_file.stream
    
    
    # onnx_file_stream.seek(0)
    # model_proto_from_stream = onnx.load_model(onnx_file_stream, onnx.ModelProto)
    # print(model_proto_from_stream.graph)
    # model_proto_bytes = onnx._serialize(model_proto_from_stream)
    # inference_session = rt.InferenceSession(model_proto_bytes)
    # onnx.save_model(model_proto_from_binary_stream, onnx_file.filename)
    
    return 'OK', 200


@app.route('/download', methods=['POST'])
def modify_and_download_model():
    # modelNodeStates = request.get_json()
    # print(modelNodeStates)
    
    
    
    
    
    return 'OK', 200

if __name__ == '__main__':
   app.run()