---
schema: qual/card@1
id: P-HKZVN
kind: problem
title: "Fix a measurable function $f : \\mathbb{R}^2 \\to \\mathbb{R}$ and, for e…"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

:::{.problem title="?"}
Fix a measurable function $f : \mathbb{R}^2 \to \mathbb{R}$ and, for every $x, y \in \mathbb{R}$, let
$$f_x : \mathbb{R} \to \mathbb{R} \text{ and } f_y : \mathbb{R} \to \mathbb{R}$$
be given by $f_x(z) = f(x,z)$ and $f_y(z) = f(z,y)$. Show that there exists such an $f$ so that $f_x \in L^1(\mathbb{R})$ for a.e. $x$ and $f_y \in L^1(\mathbb{R})$ for a.e. $y$ but
$$\int_{\mathbb{R}}\left(\int_{\mathbb{R}} f_x(y)dy\right)dx \ne \int_{\mathbb{R}}\left(\int_{\mathbb{R}} f_y(x)dx\right)dy.$$

What does Fubini's theorem imply about such $f$? What about Tonelli's theorem?
:::
