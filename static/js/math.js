MathJax = {
  includeHtmlTags: {         //  HTML tags that can appear within math
    br: '\n', wbr: '', '#comment': '', em: '', span: ''
  },

  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']],
    tags: 'ams',
    processRefs: true,
    maxBuffer: 5000 * 1024,
    
    formatError: (jax, err) => console.log(err),
    packages: {'[-]': ['noerrors']}
  },
  svg: {
    fontCache: 'global'
  }
};
