# SimpleOCR
This repo is a simple example how to use TesseractOCR to extract text from image docs. 
It provides some preprocessing functionalites for images: <a href="https://github.com/ammarali32/SimpleOCR/blob/main/preprocess.py">(Denoising, Removing lines and Fixing rotation)</a>.</br>
And Postprocessing for the text includes some basic text cleaning functions.
## Installation 
### Tesseract and leptonica
Make sure that you have installed Tesseract on your device.
#### Linux Installation
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">apt<span style="color: #333333">-</span>get install libleptonica<span style="color: #333333">-</span>dev
apt<span style="color: #333333">-</span>get install tesseract<span style="color: #333333">-</span>ocr libtesseract<span style="color: #333333">-</span>dev
</pre></div>

#### <a href="https://tesseract-ocr.github.io/tessdoc/Downloads.html">Windows Installation</a>
### Poetry 
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">pip install poetry
</pre></div></br>
For another installation options <a href="https://python-poetry.org/docs/">see</a>
### Project Installation
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">git clone https:<span style="color: #333333">//</span>github<span style="color: #333333">.</span>com<span style="color: #333333">/</span>ammarali32<span style="color: #333333">/</span>SimpleOCR<span style="color: #333333">.</span>git
cd SimpleOCR
poetry install
</pre></div>
## Testing
To run the package you have a command line interface:
<!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">poetry run python run<span style="color: #333333">.</span>py <span style="color: #333333">--</span><span style="color: #007020">input</span><span style="color: #333333">=</span><span style="background-color: #fff0f0">&quot;./coding_test/samples/oldpaper.jpg&quot;</span> <span style="color: #333333">--</span>output<span style="color: #333333">=</span><span style="background-color: #fff0f0">&quot;./output.txt&quot;</span> <span style="color: #333333">--</span>verbose
It also works <span style="color: #000000; font-weight: bold">in</span> interactive mode<span style="color: #333333">.</span>
</pre></div>
## Installation Tutorial
This is a full tutorial for installation and testing on colab.
<a href='https://colab.research.google.com/drive/1U0FtNhJhmEsls2AyYbAiTsLlJhcjIGlx?usp=sharing'>![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)</a>

## Documentation


<table class="tg">
<thead>
  <tr>
    <th class="tg-zkl2">File</th>
    <th class="tg-zkl2">Class</th>
    <th class="tg-zkl2">Method</th>
    <th class="tg-zkl2">Input</th>
    <th class="tg-zkl2">Output</th>
    <th class="tg-60hs"><span style="font-weight:bold">Comments</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fymr">run.py</td>
    <td class="tg-fymr">-</td>
    <td class="tg-fymr">run</td>
    <td class="tg-fymr">command line</td>
    <td class="tg-fymr">txt file</td>
    <td class="tg-1wig">command-line interface</td>
  </tr>
  <tr>
    <td class="tg-fymr">io_txt.py</td>
    <td class="tg-fymr">-</td>
    <td class="tg-fymr">read_file</td>
    <td class="tg-fymr">file-path</td>
    <td class="tg-fymr">Images as np.ndarray</td>
    <td class="tg-1wig">input reader</td>
  </tr>
  <tr>
    <td class="tg-fymr">io_txt.py</td>
    <td class="tg-fymr">-</td>
    <td class="tg-fymr">write_file</td>
    <td class="tg-fymr">file_path</td>
    <td class="tg-fymr">txt file</td>
    <td class="tg-1wig">output writer</td>
  </tr>
  <tr>
    <td class="tg-fymr">denoise_photos_nn.py</td>
    <td class="tg-fymr">denoisingModel</td>
    <td class="tg-fymr">Constructer</td>
    <td class="tg-fymr">-</td>
    <td class="tg-fymr">-</td>
    <td class="tg-1wig">Model trained on data from Kaggle</td>
  </tr>
  <tr>
    <td class="tg-0pky">denoise_photos_nn.py</td>
    <td class="tg-0pky">denoisingModel</td>
    <td class="tg-0pky">forward</td>
    <td class="tg-0pky">image as np.ndarray</td>
    <td class="tg-0pky">image as np.ndarray</td>
    <td class="tg-0lax">-</td>
  </tr>
  <tr>
    <td class="tg-0pky">denoise_photos_nn.py</td>
    <td class="tg-0pky">denoisingModel</td>
    <td class="tg-0pky">load_weights</td>
    <td class="tg-0pky">weights-path</td>
    <td class="tg-0pky">-</td>
    <td class="tg-0lax">-</td>
  </tr>
  <tr>
    <td class="tg-1wig">config.py</td>
    <td class="tg-1wig">CFG</td>
    <td class="tg-1wig">-</td>
    <td class="tg-1wig">-</td>
    <td class="tg-1wig">-</td>
    <td class="tg-1wig">Some parameters like weights-path and others</td>
  </tr>
  <tr>
    <td class="tg-1wig">config.py</td>
    <td class="tg-1wig">LOG</td>
    <td class="tg-1wig">-</td>
    <td class="tg-1wig">-</td>
    <td class="tg-1wig">-</td>
    <td class="tg-1wig">Logger parameters and setting</td>
  </tr>
  <tr>
    <td class="tg-1wig">preprocess.py</td>
    <td class="tg-1wig">PreProcessor</td>
    <td class="tg-1wig">Constructer</td>
    <td class="tg-1wig">CFG</td>
    <td class="tg-1wig">-</td>
    <td class="tg-1wig">-</td>
  </tr>
  <tr>
    <td class="tg-0lax">preprocess.py</td>
    <td class="tg-0lax">PreProcessor</td>
    <td class="tg-0lax">fix_rotation</td>
    <td class="tg-0lax">image as np.ndarray</td>
    <td class="tg-0lax">image as np.ndarray</td>
    <td class="tg-0lax">in case the image is rotated a little</td>
  </tr>
  <tr>
    <td class="tg-0lax">preprocess.py</td>
    <td class="tg-0lax">PreProcessor</td>
    <td class="tg-0lax">denoiseAndBinarize</td>
    <td class="tg-0lax">image as np.ndarray</td>
    <td class="tg-0lax">image as np.ndarray</td>
    <td class="tg-0lax">call the denoising model</td>
  </tr>
  <tr>
    <td class="tg-0lax">preprocess.py</td>
    <td class="tg-0lax">PreProcessor</td>
    <td class="tg-0lax">removeLines</td>
    <td class="tg-0lax">image as np.ndarray</td>
    <td class="tg-0lax">image as np.ndarray</td>
    <td class="tg-0lax">In case the image include lines</td>
  </tr>
  <tr>
    <td class="tg-0lax">preprocess.py</td>
    <td class="tg-0lax">PreProcessor</td>
    <td class="tg-0lax">preprocess</td>
    <td class="tg-0lax">image as np.ndarray</td>
    <td class="tg-0lax">image as np.ndarray</td>
    <td class="tg-0lax">call all preprocessor functions</td>
  </tr>
  <tr>
    <td class="tg-1wig">text_recognition.py</td>
    <td class="tg-1wig">textRecognition</td>
    <td class="tg-1wig">constructor</td>
    <td class="tg-1wig">language str</td>
    <td class="tg-1wig">-</td>
    <td class="tg-1wig">default is English</td>
  </tr>
  <tr>
    <td class="tg-0lax">text_recognition.py</td>
    <td class="tg-0lax">textRecognition</td>
    <td class="tg-0lax">get_text</td>
    <td class="tg-0lax">image as np.ndarray</td>
    <td class="tg-0lax">string text</td>
    <td class="tg-0lax">uses psm 1 for automatic page segmentation with OSD </td>
  </tr>
  <tr>
    <td class="tg-1wig">postprocess.py</td>
    <td class="tg-1wig">PostProcessor</td>
    <td class="tg-1wig">constructor</td>
    <td class="tg-1wig">CFG</td>
    <td class="tg-1wig">-</td>
    <td class="tg-1wig">-</td>
  </tr>
  <tr>
    <td class="tg-0lax">postprocess.py</td>
    <td class="tg-0lax">PostProcessor</td>
    <td class="tg-0lax">removeEmptyLines</td>
    <td class="tg-0lax">string text</td>
    <td class="tg-0lax">string text</td>
    <td class="tg-0lax">-</td>
  </tr>
  <tr>
    <td class="tg-0lax">postprocess.py</td>
    <td class="tg-0lax">PostProcessor</td>
    <td class="tg-0lax">cleanText</td>
    <td class="tg-0lax">string text</td>
    <td class="tg-0lax">string text</td>
    <td class="tg-0lax">remove undesirable chars "not included in CFG.chars"</td>
  </tr>
  <tr>
    <td class="tg-0lax">postprocess.py</td>
    <td class="tg-0lax">PostProcessor</td>
    <td class="tg-0lax">spellingCheck</td>
    <td class="tg-0lax">string text</td>
    <td class="tg-0lax">string text</td>
    <td class="tg-0lax">Not used but provided to use please uncomment</td>
  </tr>
  <tr>
    <td class="tg-0lax">postprocess.py</td>
    <td class="tg-0lax">PostProcessor</td>
    <td class="tg-0lax">postprocess</td>
    <td class="tg-0lax">string text</td>
    <td class="tg-0lax">string text</td>
    <td class="tg-0lax">call all postprocessor functions</td>
  </tr>
</tbody>
</table>

## Visualization and Having Fun
<a href='https://colab.research.google.com/drive/1-lpKfMfgGt8vtriDvzZp2Q6HM0ZqMLDL?usp=sharing'>![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)</a>

## References:
* https://www.kaggle.com/c/denoising-dirty-documents

