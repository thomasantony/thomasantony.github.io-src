window.MathJax = {
  AuthorInit: function () {
      MathJax.Hub.Register.StartupHook("TeX Jax Ready",function () {
        MathJax.Hub.Insert(MathJax.InputJax.TeX.Definitions.macros,{
        cancel: ["Extension","cancel"],
        bcancel: ["Extension","cancel"],
        xcancel: ["Extension","cancel"],
        cancelto: ["Extension","cancel"]
      });
    });
    MathJax.Hub.Register.StartupHook("Begin",function () {
      MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
    });
  },
  TeX: {
    equationNumbers: {
      autoNumber: "AMS",
      useLabelIds: true
    }
  },
  tex2jax: {
    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
    displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
    processEscapes: true,
    processEnvironments: true
  },
  displayAlign: 'center',
  CommonHTML: {
    linebreaks: { 
      automatic: true 
    }
  }
}
