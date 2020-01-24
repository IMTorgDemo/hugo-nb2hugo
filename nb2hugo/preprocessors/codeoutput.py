"""
This preprocessor provides for code encapsulation of output cells (```output).

For code source input, nbconvert is able to determine the kernel that is run with the cell (mostly).  In this example, it was able to get magics correct, such as %%javascript and %%r (but not %%html).  But, if I changed the default kernel (say, python to groovy), it could not decipher it.

Examples of different types of code cell outputs:

GENERAL-KERNEL
(1)
{'cell_type': 'code',
 'execution_count': 1,
 'metadata': {},
 'outputs': [{'name': 'stdout',
   'output_type': 'stream',
   'text': 'back to python\n'}],
 'source': "print('back to python')"}

MAGIC
(2)
{"cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [{
     "name": "stdout",
     "output_type": "stream",
     "text": ["back to python\n"]}],
   "source": ["print('back to python')"]}
(3)
{"cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [{
     "data": {"text/plain": ["[23, 48, 7, 'a groovy value']"]},
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }],
   "source": [
    "%%python\n",
    "from beakerx import beakerx\n",
    "beakerx.bar"
   ]}

{'cell_type': 'code',
 'execution_count': 6,
 'metadata': {},
 'outputs': [{
   'data': {'application/javascript': 'beakerx.bar = [23, 48, 7, beakerx.foo];\nbeakerx.foo'},
   'execution_count': 6,
   'metadata': {},
   'output_type': 'execute_result'}],
 'source': '%%javascript\nbeakerx.bar = [23, 48, 7, beakerx.foo];\nbeakerx.foo'}

GRAPH/IMAGE
{'cell_type': 'code',
 'execution_count': 3,
 'metadata': {},
 'outputs': [{'data': {'image/png': 'iVBORw0KG...
                        U5ErkJggg==\n',
    'text/plain': '<Figure size 432x288 with 1 Axes>'},
   'metadata': {'needs_background': 'light'},
   'output_type': 'display_data'}],
 'source': 'import matplotlib.pyplot as plt\nimport numpy as np\n\na=[x for x in range(10)]\nb=np.square(a)\nplt.plot(a,b)\nplt.show()'
 }

TABLE
{'cell_type': 'code',
 'execution_count': 5,
 'metadata': {},
 'outputs': [{'data': {'text/html': '<div>\n<style scoped>\n 
                    4\n4     5     5'},
   'execution_count': 5,
   'metadata': {},
   'output_type': 'execute_result'}],
 'source': "import pandas as pd\n\nd = {'col1': [1,2,3,4,5,6,7], 'col2': [1,2,3,4,5,6,7]}\ndf = pd.DataFrame(data=d)\ndf.head()"}


OUTPUT
%%output
writer.convert(notebook, site_dir, section)                                              
/usr/local/lib/python3.7/site-packages/nbconvert-5.5.0-py3.7.egg/nbconvert/filters/datatypefilter.
py:41: UserWarning: Your element with mimetype(s) dict_keys(['application/javascript']) is not able to be represented.
  mimetypes=output.keys())
Created 'posts/blog_test-hugo_blog.md'

"""


from nbconvert.preprocessors import Preprocessor


class CodeOutputPreprocessor(Preprocessor):
    """Preprocess the output of notebook code cells."""
    
    def preprocess_cell(self, cell, resources, index):
        """Preprocess a notebook cell."""
        if cell.cell_type == "code":
          if len(cell.outputs) > 0:
            if cell.outputs[0].output_type == 'stream':
              if type(cell.outputs[0].text) == str:  #'string':
                cell.outputs[0].text = '```output\n' + cell.outputs[0].text + '```'
              if type(cell.outputs[0].text) == 'list':
                cell.outputs[0].text[0] = '```output\n' + cell.outputs[0].text[0] + '```'
            if cell.outputs[0].output_type == 'execute_result':
              if 'text/plain' in cell.outputs[0].data:
                if type(cell.outputs[0].data['text/plain']) == str:
                  item = cell.outputs[0].data['text/plain']
                  cell.outputs[0].data['text/plain'] = '```output\n' + item + '\n```'
            if cell.outputs[0].output_type == 'display_data':  
              if 'text/html' in cell.outputs[0].data:
                if type(cell.outputs[0].data['text/html']) == str:
                  item = cell.outputs[0].data['text/html']
                  cell.outputs[0].data['text/html'] = '```output\n' + item + '\n```'

        return cell, resources