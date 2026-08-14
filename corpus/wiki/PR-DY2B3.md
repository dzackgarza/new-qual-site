---
schema: qual/card@1
id: PR-DY2B3
kind: proposition
title: "Useful properties of the Fourier transform"
classification:
  areas:
  - real-analysis
  topics:
  - fourier-analysis
  - convolution
relations: []
review: draft
---
:::{.proposition title="Useful properties of the Fourier transform"}
\[
\widehat{f\ast g}(\xi)
&= \hat f(\xi) \cdot \hat g (\xi) \\
\widehat{\tau_h f}(\xi)
&= e^{2\pi i \xi \cdot h}\widehat{f}(\xi) \\
\widehat{e^{2\pi i \xi \cdot h}f(\xi)}
&= \tau_{-h}\widehat f(\xi) \\
\widehat{f \circ T}(\xi)
&= \abs{\det T}\inv (\hat f \circ T^{-t})(\xi) \\
\dd{}{\xi} \widehat{f}(\xi)
&= -2\pi i \cdot \widehat {\xi f} (\xi) \\
\widehat{\dd{}{\xi} f}(\xi)
&= 2\pi i \xi \cdot \widehat{f}(\xi)
.\]
:::
