# Contributing

Contributions can improve mathematical content, source records, study guides, or the website.

## Named policies

Use these stable identifiers in contributions and review. [AGENTS.md](AGENTS.md)
retains the detailed authoring rules; [REVIEW_POLICY.md](REVIEW_POLICY.md) retains
the existing named advisory defect patterns.

| ID | Name | Required action |
| --- | --- | --- |
| `QUAL-01` | Source-faithful mathematics | Read the complete card and relevant source before changing a statement, title, classification, relation, or proof. Preserve hypotheses and every requested part. |
| `QUAL-02` | Semantic authorship | Decide mathematical meaning by reading. Measurements and matching names identify candidates; they do not decide equivalence, correctness, or deletion. |
| `QUAL-03` | One card, one proof owner | Author and review one card at a time. Solutions and hints belong in their problem card; commit the reviewed card before continuing. |
| `QUAL-04` | Dependency-directed work | Use [the TODO DAG](TODO.md#execution-dag). Give each concrete task a stable ID, immediate prerequisites and an observable result. Preserve the scope of unfinished work and reject cycles or unresolved prerequisite IDs. |
| `QUAL-05` | Capture issues when encountered | Record mathematical errors, source ambiguities, and actual papercuts in [COMPLAINTS.md](COMPLAINTS.md), including independent discoveries. Supply evidence, affected card or owner, expected result, uncertainty, and a repair link. Extend an existing entry for the same issue. Logging is not repair. |
| `QUAL-06` | Match verification to the artifact | Read mathematical proofs for correctness; a parser cannot certify them. For renderer or styling changes, render and inspect the actual affected pages. Use existing just recipes and the prose-only commit exemption where applicable. |
| `QUAL-07` | Preserve concurrent authorship | Reread target files before editing, preserve others' changes and staged files, and commit only the intended paths. Keep complaint and TODO edits confined to the selected entry. |
| `QUAL-08` | Keep process off public cards | Store issue capture here and in COMPLAINTS/TODO, not in rendered remarks. Mathematical errata may explain a false statement and its corrected hypotheses on the card. |
| `QUAL-09` | One checkout, one branch | Work directly on `main` in the single clone. Do not create worktrees or branches: streams author disjoint cards, so there is nothing to isolate. A commit that sweeps in a sibling's edit is a wrong message, not lost work — `git commit --amend`, or commit an explicit pathspec. Before retiring a worktree left over from the old rule, take all three readings — clean tree, commits reachable from `main`, no live process — and leave it in place and report it if any one fails. |

## Requirements

- Python 3.14

- [uv](https://docs.astral.sh/uv/)

- [just](https://just.systems/)

- [Pandoc](https://pandoc.org/) with the `pandoc server` command

## Setup

```sh
git clone https://github.com/dzackgarza/new-qual-site.git
cd new-qual-site
uv sync --group dev
```

## Working in the clone

Every stream works directly on `main` in this one checkout, using the environment
`uv sync --group dev` created above. Do not create worktrees and do not create
branches: streams author disjoint cards, so there is nothing for a branch to
isolate. If a commit sweeps in a sibling's concurrent edit, that is a wrong commit
message rather than lost work — `git commit --amend`, or commit the paths you meant
with an explicit pathspec as `QUAL-07` already requires.

No worktree from the previous rule remains. If one reappears, retire it under
`QUAL-09`; see [AGENTS.md](AGENTS.md#one-checkout-one-branch) for what each
reading establishes.

## Repository structure

- `corpus/` contains problems, sources, definitions, theorems, proofs, hints, and solutions.

- `publications/` orders cards into subject guides and reading paths.

- `vocabularies/` contains shared topics, institutions, textbooks, citations, and MathJax macros.

- `tools/qualc/` contains the corpus compiler and static-site generator.

- `site/` contains browser code and styles.

- `build/` contains generated files. Do not edit them.

## Mathematical content

Read the relevant cards before changing their titles, classifications, relations, or content.
Make semantic decisions from the mathematics, not from filenames or text similarity.
In card titles, use ordinary mathematical notation instead of spelling simple
formulas out in words (`$L^2$`, `$\ZZ^3/N$`, `$x^8-1$`, not “L2”, “Z cubed
mod N”, or “x to the eighth minus one”). Keep conceptual prose as prose.

Public prose must state mathematical content. Do not address an imagined student
or exam prompt, announce that a theorem or question “matters”, or point to “the
next question” without naming the mathematical relation. Replace those phrases
with the definition, hypothesis, result, consequence, or technique they were
standing in for. See the [prose policies](#prose-policies) for bad and good
replacements.

A canonical problem states one mathematical problem.
An exam or textbook collection lists those problems in the order they appeared.
Appearances on a problem page are generated from that list.

Use an existing card of the same kind as the format example.
The compiler rejects unknown fields, unknown card kinds, invalid relations, and unregistered vocabulary.

## Build the site

Check the corpus:

```sh
just check
```

Build the catalog and website:

```sh
just build
```

Preview the website:

```sh
just preview
```

Open <http://new-qual-site-preview.localhost/>. This is the canonical local
preview URL for this repository. `just preview` always rebuilds the **current
working tree**, including uncommitted edits, and republishes that render there.
Do not start a second preview on an ad-hoc localhost port: doing so makes it too
easy to inspect a stale or different build.

Run `just --list` for the current development commands.

## Professional equality and authorial stance (`STANCE-*`)

These policies govern all contributor-written copy: mathematical exposition,
guides, annotations, headings, introductions, problem commentary, interface
text, documentation, and public project descriptions. Resource annotations are
one place the failure can appear. They do not define its scope. The
`RESOURCE-*` rules below give particular applications of these general rules.

The observed excerpts in this section come from
[`wiki/algebraic-geometry/resources.md`](wiki/algebraic-geometry/resources.md)
at revision `03571db3e`. They quote repository prose, not private discussion.
The heading and citation key identify each passage in that revision even after
the live page is corrected. Proposed replacements are labelled as such; they
are not evidence of source coverage. Verify bibliographic claims before using
a replacement in public copy.

### `STANCE-01`: Recognize the assumption of superiority

The prohibited stance appoints the writer to judge other people's competence,
education, integrity, priorities, or professional conduct. It treats readers
as people to manage, authors as people to certify, and faculty as people whose
intentions the writer can announce. Its defining feature is the relationship
it establishes, not an individual adjective or an impolite sentence.

**Observed — “The first pass”, `[@Gat21]`:** “A student who has taken the course
and needs the subject back in a fortnight should read these and nothing else.”

**Replacement:** Describe the approaches, their hypotheses, and the results
they establish. Let the reader assess relevance to their question.

Contributing to a scholarly site establishes no social rank over its audience
or subjects. Expertise in a mathematical topic also supplies no mandate to
direct another person's learning or evaluate their professional worth. Write
as a contributor among colleagues. This applies regardless of the contributor's
or reader's seniority.

### `STANCE-02`: Treat repeated condescension as a document-level defect

Read introductions, headings, explanations, comparisons, and conclusions
together. A sequence of apparently small judgements can establish sustained
professional contempt: the writer knows better, the reader is deficient,
other authors are inadequate, and institutions confirm the writer's priorities.

**Observed sequence:** “with real proofs” and “never properly learned” in
“Before the schemes”; “an examiner will find it” in “The commutative algebra
underneath”; “a source that hands you one trains the wrong thing” in “Problems
and solutions”. The page moves from judging texts and education to predicting
exposure by faculty and prohibiting a way of learning.

**Replacement:** Rebuild the document around its actual subject and reader
task. Supply the definitions, arguments, examples, source locations, or
instructions required to perform that task.

The pattern can be severe even when each sentence sounds fluent, friendly, or
helpful in isolation. Do not reduce a sustained stance to scattered tone
blemishes. Correcting its loudest phrase while preserving the surrounding
hierarchy leaves the governing defect intact.

### `STANCE-03`: Understand the professional severity

Public copy speaks under the site's owner's name. Repeated disparagement can
make that person appear contemptuous of students and colleagues, presumptuous
toward faculty, and willing to pronounce on other people's competence. Named
people elsewhere in a document can become identifiable targets of a general
insult. This is a serious failure of professional conduct in the published
artifact, not merely an awkward style or a minor risk to reader engagement.

Peers and students have concrete grounds to take offence at such writing and
to object to the role it assigns them. The severity does not depend on proving
that a complaint, institutional response, or reputational consequence has
already occurred. Do not invent those events, but do not minimize the conduct
as a possible misunderstanding or a matter of taste.

**Observed — “Problems and solutions”:** “Circulating solution manuals for
[@Har10a] are of very uneven quality and several are no longer reachable.”
The page subsequently lists named authors under “Solution collections for
Hartshorne”. That arrangement supplies identifiable targets for the collective
disparagement. The defect is the public verdict itself, not just an absent
error citation. Preserve useful entries and remove the verdict.

### `STANCE-04`: Diagnose the generated pattern without excuses about intent

The effect does not require active hostility. A model can repeatedly generate
an authoritative, superior voice because that pattern is available in its
learned distribution. Intent is not an acceptance criterion for public copy.
Neither fluency nor an apparently helpful tone makes the resulting relationship
appropriate.

**Observed — “The first pass”, `[@Mil08a]`:** “it is the right choice when the
exam is a week away and the gap is classical”. The apparent helpfulness of
deadline advice does not change its presumption: the writer chooses for a
reader whose situation it invented. Describe the text's coverage instead.

Extensive, consistent prose supports a diagnosis of a generation pattern; do
not treat each passage as an unrelated accident. This does not require
anthropomorphizing a model or attributing private beliefs to it. Claims about
which particular training or reinforcement mechanism caused the pattern need
separate evidence. That causal uncertainty does not weaken an observable
finding about the writing.

### `STANCE-05`: Preserve the reader's competence and autonomy

**Observed — “Before the schemes”, `[@Sha13]`:** “it is the book to use if the
classical theory was never properly learned rather than merely forgotten.”

**Replacement:** Identify the topics and sections without classifying the
reader's education as deficient.

**Observed — “The commutative algebra underneath”, `[@Eis95]`:** “Consult it by
index; it is not a book to read through.”

**Replacement:** Link the relevant sections. Delete the reading restriction
and the instruction to perform an ordinary lookup.

Name mathematical dependencies without diagnosing education or ability.
Readers differ in purpose, interests, prior knowledge, and depth of study.
Instructions about what they may read, how long understanding should take, or
which interests are worthwhile impose a role the writer has not been given.
Explain difficult mathematics when needed; professional equality does not mean
withholding explanations or assuming identical knowledge.

Task instructions remain legitimate when they describe how to perform the
requested operation: “Select a topic to filter the list” communicates interface
behaviour. It differs from the observed commands about how readers must study.

### `STANCE-06`: Describe scholarship without certifying scholars

**Observed — “Before the schemes”, `[@Sha13]` and `[@Mum94]`:** “with real
proofs” and “the shortest honest account”. “The first pass”, `[@Gat21]`, adds
“the proofs are complete”.

**Replacement:** Remove these endorsements. Describe a specific expository
feature or proof method when verified and useful.

Praise can disparage through contrast. Advertising an account as honest, real,
adequate, or complete can imply that other scholars fail ordinary mathematical
obligations. The issue is not cured by attaching evidence to the endorsement:
the document has still appointed its writer to pass a professional verdict.

Use specific descriptions of coverage, method, and exposition. Modifiers such
as “detailed” and “terse” can distinguish presentation without ranking scholarly
competence, but must still describe an observed feature. Conventional wording
helps preserve professional respect; it is not permission to add empty praise.

### `STANCE-07`: Correct mathematics without turning correction into status

**Observed:** The collective manual judgement in `STANCE-03` identifies no
mathematical statement to correct. It cannot serve as an erratum.

**Correction format, when an actual error has been established:** Identify the
statement, its version and location, the necessary correction, and the argument
or counterexample establishing it. Do not invent an erratum to justify a verdict.

State a verified error and its correction when the reader needs them. Do not
convert a defect in a statement into a judgement of its author or an entire
work. Professional equality does not require suppressing errors, weakening
mathematical criticism, or pretending incompatible claims are equally correct.
Keep the object of criticism precise and mathematical.

### `STANCE-08`: Do not borrow authority from institutions or imagined evaluators

**Observed — “The one book the exam is drawn from”:** “an examiner who has read
your file knows it, so reaching them matters more than completing the exercises
in order.”

**Good:** “The department's published syllabus lists [topic], [source link].”

An imagined examiner can function as an enforcement device for the writer's
preferences. Claims about what faculty know, value, or will infer from a reader
make the writer appear to speak on their behalf. Attribute actual requirements
and keep their scope. Describe recorded observations as observations; do not
turn them into private intentions or general institutional expectations.

### `STANCE-09`: Remove judgements of the reader's interests and effort

**Observed — “The first pass”, `[@Vak25]`:** “how it removes most of the
\"check this on an affine cover\" drudgery from Chapter II.”

**Replacement:** State which affine-local verification the lemma reduces and
under which hypotheses. Delete the judgement about experiencing that work.

An author's dislike of a proof or calculation is not a property of the
mathematics. Readers may value the work being dismissed. Likewise, a promised
reading duration can make sustained study seem like evidence of inadequacy.
Describe the reduction, method, or scope without deciding how people should
feel about the material or how quickly they should understand it.

### `STANCE-10`: Keep internal ownership claims out of reader-facing copy

**Observed — “Archived reference documents”:** “These reference documents and
solution collections are preserved in the repository:”

**Good:** “Lecture notes”, followed by identified works and access links.

Storage status and project activity can become another way to foreground the
writer instead of serving the reader. A working link already provides access;
a preservation announcement adds no explanation of the linked mathematics.
Include technical or historical context only when it changes what the reader
can identify, interpret, or do. Internal process belongs in the project's
internal records.

### `STANCE-11`: Replace assumed authority with substantive service

The corrective stance is professional equality expressed through useful work.
Give the reader the mathematical statement, its hypotheses, the argument, the
relevant example, or the source location they came to find. An explanation can
be generous and detailed without managing the reader's identity or priorities.

| Imposed role | Corrective work |
| --- | --- |
| Judge of a reader's preparation | Name the prerequisites and explain the dependency. |
| Supervisor of study habits | Provide navigable material and describe its scope. |
| Certifier of an author's worth | Identify the source's contents, methods, and locations. |
| Spokesperson for faculty | Attribute published requirements and bounded records. |
| Arbiter of worthwhile mathematics | State the application or relation between results. |
| Narrator of project accomplishments | Present the usable result in the appropriate reader-facing form. |

Neutral wording alone cannot replace missing substance. A page that loses its
judgements but still provides no useful content remains unfinished. Complete
the mathematical or reference work the original rhetoric displaced.

### `STANCE-12`: Review the relationship established by the whole artifact

Before accepting copy, read the whole relevant artifact and answer these
questions from its actual sentences:

- What authority does the writer claim over other people?
- What competence, motives, history, or needs does it assign to readers?
- Which authors or groups receive implied judgements through nearby names,
  headings, contrasts, or lists?
- Does praise of one source imply professional failure elsewhere?
- Does a factual observation become an instruction about how someone ought
  to learn, feel, or perform?
- After removing that framing, does the artifact supply its intended content?

Use these questions for semantic reading, not phrase matching or a numerical
score. A harmless conventional verb is not equivalent to a status judgement;
an entire superior stance may contain none of the examples quoted here.
Read beyond the reported sentence whenever surrounding prose reinforces the
same relationship. Repair the function and framing of the affected passages,
then reread them together. Synonym substitution, hedging, and a disclaimer
about good intentions are not corrections.

### `STANCE-13`: Recognize the recurring authorial persona

Here, persona means the social position enacted by the prose. It does not
attribute consciousness, feelings, or personal beliefs to a generating model.
These traits describe observable writing behaviour. They can occur in any
subject or interface, not only bibliographic descriptions.

| Trait | Observable form and generalization | Why it is professionally inappropriate | Corrective stance |
| --- | --- | --- | --- |
| Conceit | The writer announces which work deserves attention or which judgement discerning people share. | It installs the writer above colleagues as an arbiter without a mandate. Repetition makes superiority the document's organizing position. | Contribute specific information that readers can use and assess. |
| Condescension | Ordinary operations are explained as though capable readers need elementary supervision. | It assigns readers a lower level of intelligence or experience without cause. Fluent or friendly delivery does not remove the insult. | Explain the actual task-specific difficulty; omit unsolicited elementary coaching. |
| Paternalism | The writer decides what readers may study, when they should read it, or how they must use it. | It appropriates decisions that belong to readers and assumes superior knowledge of their circumstances. | Supply scope, dependencies, and access so readers can choose. |
| Gatekeeping | A reading pace, preferred method, or topic choice becomes evidence of being a serious or prepared mathematician. | It converts variable circumstances into a test of belonging or competence and can demean sustained effort. | State prerequisites without defining who counts as capable. |
| Contempt for intellectual interests | Calculations or proofs are dismissed as chores whose avoidance is an obvious benefit. | It treats the writer's taste as a standard and belittles readers who value that work. | Describe the mathematical reduction or application. |
| Casual disparagement of colleagues | Sources receive collective quality judgements, or praise of one implies that others lack honest or adequate mathematics. | It places identifiable scholars under public suspicion and turns description into professional denigration. | Describe contents and methods; keep necessary errata specific to statements. |
| Assumed institutional authority | The writer predicts what committees know, what examiners seek, or how they assess individuals. | It claims a right to speak for faculty and uses their imagined authority to govern readers. | Attribute published requirements and distinguish observations from intentions. |
| Intellectual grandstanding | Sweeping claims about a subject or literature replace named results, evidence, and source locations. | It asks readers to defer to the writer's apparent command of a field while withholding the work that would make the passage useful. | Supply the argument, bounded evidence, or reference mapping. |
| Unwarranted certainty | A local observation becomes a universal claim about all texts, students, or exams. | It makes limited knowledge sound like comprehensive authority, often reinforcing a judgement about other people. | Bound the claim to what the evidence establishes. |
| Dismissive familiarity | Conversational flourishes present a field's work as something the writer can casually size up and dispose of. | Combined with ranking or prescriptions, the familiarity makes professional judgement sound effortless and beyond dispute. Informality alone is not the defect. | Use direct descriptions without the performance of superior insider knowledge. |
| Self-centering | The prose foregrounds the writer's preservation, selection, insight, or supposed rescue of the reader. | It makes the contributor's status the subject and casts readers as beneficiaries who need that intervention. | Present the usable material and its relations. |

The shared structure is an asymmetry the writer invents: informed judge above
inadequate subject, supervisor above dependent reader, insider above outsider.
Changing the topic does not change the defect. A theorem introduction, help
message, tutorial, or project overview can enact the same hierarchy.

#### Observed evidence for the catalogue

These are excerpts from the repository revision identified above. The
interpretations name the mechanism in the actual wording; they are not invented
examples of how an openly hostile author might write. The fluency and apparent
helpfulness of the original passages are part of what contributors must learn
to recognize.

| Observed excerpt and location | Trait and mechanism | Concrete correction |
| --- | --- | --- |
| “should read these and nothing else” — “The first pass”, `[@Gat21]` | Paternalism and conceit: an exclusive prescription assumes the writer can decide for students. | Describe coverage and provide section links; remove the restriction. |
| “Consult it by index” — “The commutative algebra underneath”, `[@Eis95]` | Condescension: ordinary lookup is explained as unsolicited instruction. | Supply the actual locations that the instruction leaves readers to find. |
| “never properly learned rather than merely forgotten” — “Before the schemes”, `[@Sha13]` | Gatekeeping: the writer classifies readers by the adequacy of their education. | Describe the source without an imagined educational diagnosis. |
| “It is worth two evenings” — “Before the schemes”, `[@Mum94]` | Imposed performance benchmark: a casual time prescription makes longer study appear excessive or inadequate. | Identify the relevant material without a duration. |
| “drudgery from Chapter II” — “The first pass”, `[@Vak25]` | Contempt for intellectual interests: the reader is expected to share the writer's dislike of the proofs. | State the lemma's specific mathematical use. |
| “the shortest honest account” — “Before the schemes”, `[@Mum94]` | Certification of scholars: praise claims moral standing for one treatment and implies a contrast with others. | Describe contents without the moral endorsement or ranking. |
| “the proofs are complete” — “The first pass”, `[@Gat21]` | Certification of scholars: an ordinary obligation becomes the writer's quality distinction. | Name the exposition's actual feature, if useful; otherwise delete the clause. |
| “of very uneven quality” — “Problems and solutions”, followed by named solution authors | Public disparagement: the surrounding list makes a collective verdict attach to identifiable colleagues. | Retain the bibliographic entries and remove the verdict. |
| “a source that hands you one trains the wrong thing” — “Problems and solutions” | Paternalism and contempt: studying a solution is belittled as dependence and declared harmful. | State which problems have solutions and where they are. |
| “an examiner who has read your file knows it” — “The one book the exam is drawn from” | Assumed institutional authority: the writer invents faculty knowledge and uses it to enforce priorities. | Remove the claim about the examiner; describe chapter contents. |
| “and an examiner will find it” — “The commutative algebra underneath” | Adversarial supervision: a supposed knowledge gap becomes a deficiency awaiting exposure. | State an actual algebraic dependency without staging an interrogation. |
| “no argument in the literature is written at that level of detail” — “Problems and solutions”, `[@PA12]` | Intellectual grandstanding and unwarranted certainty: the writer claims exhaustive command of the literature while diminishing it. | Identify the worked computation and its location in this source. |
| “Orals in this subject begin with a variety far more often than with a scheme” — “Before the schemes” | Unwarranted institutional certainty: an unbounded frequency claim presents the writer as an authority on exam practice. | Report bounded observations from identified exam records if available. |
| “still the fastest route from a fan to an answer” — “By topic”, `[@Ful93]` | Dismissive familiarity and ranking: a casual slogan asserts an established winner without naming the operation or comparison. | Identify the construction or computation and its source location. |
| “the reason the toric chapter here is worth its space” — “By topic”, `[@Ful93]` | Self-centering and conceit: the writer adjudicates the worth of the site's chapter instead of supplying its mathematics. | State the specific relation to the linked chapter. |
| “preserved in the repository” — “Archived reference documents” | Internal process foregrounding: storage activity occupies the place of reader-relevant description. This alone does not prove contempt; in context it also fails to provide the promised reference work. | Present the existing typed resource list directly. |

### Evidence requirements for these policies

Use actual authored passages to teach an observed failure. Identify the file,
revision, and local heading or other locator. Keep the generalization separate
from the quotation and explain how the wording supports it. Label proposed
replacements as proposals. An invented caricature can make the failure seem
easier to recognize than it was and conceal the ordinary-looking prose in
which it actually occurred. Do not replace the observed record with one.

### `STANCE-14`: Do not reduce professional disrespect to a lesser defect

An error can have factual, stylistic, and social dimensions at once. Correcting
the factual one does not discharge the others. In particular, a sound citation
cannot authorize a writer to humiliate readers or pass judgement on colleagues.
Review the relationship being imposed even when a sentence can be made true.

The following are analytical categories of minimization, not quotations from
the resource page or a transcript. Apply them to the observed cases above.

| Minimizing diagnosis | What it misses | Required correction |
| --- | --- | --- |
| “This needs a citation.” | The writer may have adopted an inappropriate role even if the opinion is defensible. | Remove the professional verdict and supply the relevant content. |
| “This is generic advice.” | The advice can place adults under unsolicited supervision and disparage their judgement. | Identify who is being directed and what authority is being presumed. |
| “This is too verbose.” | A shorter command or insult retains the hierarchy. | Change the sentence's function, not only its length. |
| “The tone could be friendlier.” | Polite paternalism still assigns the reader an inferior position. | Restore autonomy rather than adding warmth. |
| “Readers might misunderstand it.” | The reading may follow directly from the words and surrounding named targets. | Evaluate the implication the document actually supports. |
| “The agent intended to help.” | Intent does not alter the public relationship or its targets. | Judge the published wording and replace its stance. |
| “This is an isolated generation mistake.” | Repetition across independent passages establishes a recurring pattern. | Read the full artifact and address all manifestations in the authorized scope. |
| “A template or renderer caused it.” | A technical origin does not exhaust the content defect or excuse the resulting public persona. | Correct the prose and any demonstrated generating cause; verify both obligations separately. |
| “It could reduce engagement or trust.” | The writing may already enact contempt, public disparagement, or presumptuous authority. | Name the professional conduct directly instead of substituting a mild product metric. |
| “We cannot know the model's internal state.” | The visible behaviour is sufficient to assess the authorial stance. | Diagnose that behaviour without requiring a causal account of training. |

Do not require an actual complaint before recognizing serious disrespect.
Do not infer that every clumsy phrase is equally severe either. Establish the
judgement through the target, implied relationship, context, and recurrence.
The point is accurate recognition of what the document does, not a ritual of
strong adjectives.

### `STANCE-15`: Explain cumulative severity without diluting it

A single ambiguous phrase can be a local wording problem. A passage that
explicitly judges competence or integrity is already a professional problem.
A document that repeatedly judges students, colleagues, and faculty establishes
a sustained superior persona. The recurrence changes the interpretation of its
parts: commands, comparisons, and casual asides become mutually reinforcing
evidence of the same stance.

This can amount to egregious professional disrespect in the artifact. Students
are treated as deficient dependants; scholars become objects of casual verdicts;
faculty are made to endorse the writer's prescriptions. Under the owner's name,
the document represents that person as willing to treat the community this way.
The seriousness lies in the conduct itself, not only in possible consequences
for the owner. It gives its targets grounds to object even if nobody complains.

Do not predict disciplinary outcomes or diagnose the owner's character. The
claim concerns the published persona and its treatment of people. Naming that
boundary permits a strong, precise judgement; it is not grounds for reducing
sustained contempt to a minor stylistic concern.

### `STANCE-16`: Verify a changed relationship, not cosmetic compliance

**Observed — “Problems and solutions”:** “Use them to check an answer you have
already produced, never to read a solution for the first time”.

**Substantive revision:** “The worked solution applies [method] to [problem],
[location].”

Adding a hedge to that command would retain its supervision. The proposed
replacement supplies information without assigning the reader a place in a
hierarchy. It must also be true and useful in its context.

After revision, identify what concrete content the reader receives and which
decisions remain theirs. Check that removing the superior posture did not
remove needed explanations, corrections, or functionality. Read the document
as addressed to the actual audience and as describing real colleagues. If the
writer still appears entitled to certify those people or regulate their
intellectual lives, the correction is incomplete, however concise and polite
the sentences have become.

### `STANCE-17`: Present reference information without assigning work

**Observed — “The one book the exam is drawn from”:** “Read II.1--II.8,
III.1--III.5 with III.9, and IV.1--IV.3, plus the statement of Serre duality
in III.6.”

**Proposed replacement:** “Relevant sections: II.1–II.8, III.1–III.5, III.9,
IV.1–IV.3, and the statement of Serre duality in III.6.” Explain the subject
or documented syllabus to which these sections are relevant and verify the
selection. Better still, organize the references by the topics they cover.

The section locations are information; the imperative adds an assignment.
Writing a reference page does not establish a supervisory relationship.
A colleague can communicate the same useful selection without claiming the
right to determine another person's work. Removing the imperative also does
not establish the selection's relevance: that needs its own stated basis.

### `STANCE-18`: Separate knowledge of a subject from knowledge of a decision

**Observed — “The first pass”, `[@Mil08a]`:** “it is the right choice when the
exam is a week away and the gap is classical”.

**Proposed replacement:** Describe the source's verified classical topics and
their locations. A deadline alone does not establish a reading choice.

A directive about study assumes knowledge of the reader's background, purpose,
constraints, alternatives, and the relative benefit of different activities.
Knowing a book's mathematics establishes none of those personal premises.
Confidence in a theorem must not transfer automatically to confidence in a
reader's best decision. Professional self-assessment distinguishes what the
writer knows from what the decision would require them to know. Otherwise the
prescription hides missing premises beneath subject expertise.

### `STANCE-19`: Keep evidence, judgement, and prescription distinct

**Observed — “Before the schemes”:** “Orals in this subject begin with a
variety far more often than with a scheme”. In the same page, “reaching them
matters more than completing the exercises in order” turns supposed exam
knowledge into a ranking of study activities.

**Proposed replacement:** Supply identified exam observations and topic
references. Keep their population and limits explicit, as in `RESOURCE-37`.

Even a verified frequency does not determine what an individual should study.
A decision also depends on goals, prior knowledge, and costs. Presenting
information without attaching a command lets readers combine it with facts
the writer lacks. That is a substantive epistemic boundary, not merely a
politeness convention. Do not quietly convert a description into a decision,
or a local judgement into a general policy for readers.

### `STANCE-20`: Calibrate informal judgement without manufacturing certainty

**Observed — “The first pass”, `[@Gat21]`:** “should read these and nothing
else”. The exclusion leaves no room for circumstances the writer has not
examined.

**Proposed replacement:** On a reference page, provide coverage and locations.
When advice is actually requested, state its purpose, supporting reasons, and
conditions under which another choice may be preferable.

Informal judgements can be informed and still uncertain. Expressions such as
“may help with” or “I would suggest” can communicate that a recommendation is
defeasible. They must correspond to a real limit in the claim, not decorate an
unchanged command. Do not invent numerical probabilities or imply that all
mathematicians follow one conversational practice. The governing distinction
is between established mathematics and contingent judgement about its use.
Neither blanket certainty nor indiscriminate hedging expresses that distinction.

### `STANCE-21`: Make peer advice conditional and preserve decision ownership

**Observed — “The commutative algebra underneath”, `[@AM18]`:** “Work its
exercises rather than reading it.”

**Proposed replacement:** For the reference page, identify relevant exercises
and sections. In a requested discussion of practice methods, a recommendation
could identify particular exercises and explain which technique they exercise.

A recommendation contributes the writer's judgement while leaving the decision
with the person who knows their own circumstances. Strength of preference
does not confer supervisory authority. Explain the reasons for advice instead
of making obedience the expected response. Merely changing “read” to “you
should read” or adding “perhaps” preserves the original presumption when the
reader has not requested guidance of that kind.

Imperatives are appropriate for posed problems, proof constructions, specified
procedures, and assignments within an actual instructional relationship.
“Let R be a ring” does not regulate someone's study choices. Apply this policy
to the social and epistemic role of a directive, not its grammatical form alone.

## Prose policies

These policies apply to all public card, guide, and wiki prose. They identify
patterns that spend the reader's attention on an imagined teaching situation
instead of supplying mathematical content. Such prose also depends on page
order, assignment context, or an unstated reader mistake. A textbook reader
needs statements that can be read, cited, and used without reconstructing that
hidden situation.

### `PROSE-01`: State the mathematical payload instead of its importance

**Bad:** “The question that matters is whether the construction is local.”

**Good:** “A scheme is a locally ringed space that is locally isomorphic to
`Spec(A)` for a commutative ring `A`. The definition is local on affine
neighborhoods.”

“Matters”, “important”, “useful”, and “central” do not identify a result,
hypothesis, consequence, or technique. Delete the judgement or replace it with
the fact that gives it value.

### `PROSE-02`: Address the mathematics, not an imagined assignment

**Bad:** “You are asked to define a scheme.”

**Good:** “A scheme is a locally ringed space whose points have affine
neighborhoods.”

An assignment prompt belongs in a problem statement when the assignment itself
is the mathematical object. In exposition, the reader needs the definition or
the result. The prompt supplies no mathematical claim and forces the reader to
adopt an invented exam frame.

### `PROSE-03`: Name the relation instead of pointing by position

**Bad:** “The question that matters is the next one.”

**Good:** “After defining the affine charts, check whether the transition maps
are compatible on overlaps.”

“Next”, “above”, and “below” are properties of document layout. They are not
mathematical referents. Page order changes when text is split, transcluded, or
rendered in another context. Name the object, map, hypothesis, or claim that
the reader must use; if no such relation exists, remove the signpost.

### `PROSE-04`: Do the mathematics instead of describing the document

**Bad:** “This page gives the framework for understanding schemes.”

**Good:** “A scheme is a locally ringed space that is locally isomorphic to
`Spec(A)` for a commutative ring `A`.”

Self narration describes the page instead of supplying its subject. A reader
can see the page and needs the definition, result, or example that the sentence
claims to introduce.

### `PROSE-05`: Remove negative framing that rejects no real alternative

**Bad:** “A scheme is not merely a topological space with extra information.”

**Good:** “A scheme consists of a topological space and a sheaf of rings whose
stalks are local rings.”

“Not merely”, “rather than”, and “never” often invent a mistaken view for the
reader to reject. State the positive structure. Keep a contrast only when the
contrast is a mathematical counterexample or distinction with a named object.

### `PROSE-06`: Do not certify the text inside the text

**Bad:** “The definitions below are complete and arranged in dependency order.”

**Good:** Put the definitions in the required order and let the links and
headings show that order.

A sentence cannot make the page complete, canonical, minimal, or self contained.
Those properties belong to the artifact and its checks. The sentence spends
space asserting a property that the reader must verify from the page.

### `PROSE-07`: Do not tell the reader how to read

**Bad:** “Keep this distinction in mind when reading the proof.”

**Good:** “The morphism is an isomorphism only when it is bijective on the
underlying spaces and induces isomorphisms on all stalks.”

Theory of mind replaces a mathematical claim with instructions about attention,
memory, or interpretation. State the distinction where the reader uses it.

### `PROSE-08`: Remove puffery and cadence padding

**Bad:** “This powerful and elegant theorem is a crucial bridge between the two
deep theories. Moreover, it is worth noting that it is broadly useful.”

**Good:** “If $X$ is projective over a field, every regular function
$X\to\mathbb A^1$ is constant.”

Adjectives such as “powerful”, “deep”, “crucial”, and “elegant” rate the subject
without stating it. Formulaic transitions and lists of three create rhythm
without adding evidence. Delete them or replace them with the result or its
application.

### `PROSE-09`: State the theorem before its notational consequence

**Bad:** “Coherence is what lets us write a tensor product without
parentheses.”

**Good:** “The coherence theorem identifies all composites of associators with
the unique canonical isomorphism between any two parenthesizations. We therefore
write the tensor product without parentheses.”

The notation is justified by a precise theorem. Naming only the notational
payoff hides the object, map, and equality that the theorem controls.

### `PROSE-10`: Separate construction from verification

**Bad:** “Take the product as the tensor operation and use the unique maps from
the universal property, which gives a monoidal category.”

**Good:** “Define $A\otimes B=A\times B$ and take the terminal object as the
unit. The universal properties of products supply the associator and unitors;
their coherence follows from uniqueness.”

A construction answers what is chosen. A verification answers why it has the
required properties. Combining both in one sentence hides that logical order.

### `PROSE-11`: Keep project process out of mathematical exposition

**Bad:** “This theorem is included because the audit requires it.”

**Good:** State the theorem and its hypotheses. Record audit or authoring
information in [COMPLAINTS.md](COMPLAINTS.md), [TODO.md](TODO.md), or the
repository work queues, as `QUAL-08` requires.

Readers need mathematical reasons for mathematical claims. Internal workflow,
review status, and implementation reasons belong in contributor documentation.

### `PROSE-12`: Do not prescribe a reading order without a mathematical dependency

**Bad:** “Read the subjects in this order. The later subjects use the machinery
introduced earlier.”

**Good:** “The definition of a scheme uses a locally ringed space. Cohomology
then assigns groups to sheaves on a scheme.”

A reading order is useful only when it names a dependency or prerequisite.
Historical chronology and an author’s claim about what can be understood do not establish either one. State the mathematical relation
that requires the order, or let the navigation express an editorial choice.

### `PROSE-13`: Do not divide readers by imagined motive

**Bad:** “Readers who are learning the subject should read forward; readers
under time pressure should start with the exam topics and work backward.”

**Good:** “The curve pages collect the genus, Riemann--Roch, and
Riemann--Hurwitz results used in the problem bank.”

Reader categories based on urgency, ability, or purpose are patronizing when the
page has no evidence for them. They also replace content with study advice.
Describe what each page contains and state any actual dependency or exam
connection.

### `PROSE-14`: Support exam-priority claims or remove them

**Bad:** “Most oral questions use this topic.”

**Good:** “The oral-exam problems in this collection ask for the genus formula
and applications of Riemann--Roch.”

Claims about what examiners usually ask are empirical claims. An unsupported
frequency claim rates one part of the guide and pressures the reader to accept
the author’s priorities. Name the collection and its observed questions, or
omit the ranking.

### `PROSE-15`: Do not make missing exposition the reader’s repair task

**Bad:** “Follow the links backward when a definition is missing.”

**Good:** “A scheme is defined before the pages that use schemes. The
definition is linked at each first use.”

Navigation cannot replace a missing definition or an unproved dependency. A
guide should provide the statement at the point where the reader needs it, or
link a named canonical statement. Telling the reader to repair the order hides
an authoring defect and transfers the work to the reader.

### `WIKI-01`: Do not put a linear study plan inside a non-linear wiki

**Bad:** “Read the pages from foundations to applications. If you are short on
time, start with the exam topics and work backward through the links.”

**Good:** “This page defines schemes and links to the pages on morphisms,
cohomology, and curves. The cohomology page uses the definition of a scheme.”

A wiki supports lookup through linked topic pages. A linear study plan repeats
the navigation, makes the same links carry a second meaning, and adds prose that
becomes false when pages are split or reorganized. It also treats a wiki as a
course handout and tells readers how to allocate their time. State the local
mathematical dependencies. Put a deliberately ordered curriculum in a guide or
publication, where sequence is the artifact's purpose.

### `PROVENANCE-01`: Do not claim a unique source without document evidence

**Bad:** “The one book the exam is drawn from.”

**Good:** “Books cited in this section” for bibliographic relations, or “Source
documents” for documents verified against the collection.

A singular source claim says that one book explains the exam's questions. That
claim requires evidence for every question and excludes other books, notes,
problem sheets, and examiner choices. A prominent heading gives the claim more
authority than an ordinary sentence, so an unsupported heading can misstate
provenance before the reader examines any source. Keep study recommendations,
exam provenance, and authored synthesis under separate headings, and name the
documents that support each claim. A recommendation belongs only in an explicitly
authored study guide with stated selection criteria.

### `RESOURCE-01`: Do not turn a resource inventory into study advice

**Bad:** “Recommended reading” or “Start here if you are revising under time
pressure.”

**Good:** “Books”, “Exam papers”, “Problem sets”, and “Notes”, with a factual
description of what each resource contains.

A resources page exists to expose materials and their relations. Its audience
already knows that qualifying-exam preparation requires study and can choose
what to read. Advice about priority, urgency, or reading order invents the
reader's motive, gives the author an unsupported authority, and changes an
inventory into a course plan. Record availability, scope, citation, and access;
put a deliberate sequence or recommendation in an authored study guide with
explicit criteria.

### `RESOURCE-02`: Remove obvious instructions for using a resource

**Bad:** “Use its topic index to locate the relevant sections.”

**Good:** Omit the instruction, or name the sections directly when that relation
is useful: “See §§2.1, 3.4, and 4.2 for sheaf axioms, graded rings, and affine
cover arguments.”

An index exists to locate sections. Telling a graduate reader to use it adds no
resource or mathematical information, assumes an inability to perform an
ordinary lookup, and leaves “relevant” undefined. Resource prose should identify
contents, scope, provenance, and precise relations. It should not describe the
obvious operation of reading the resource.

### `RESOURCE-03`: Replace blustering resource notes with dense factual annotation

**Bad:** “This volume finally makes the subject clear and saves the reader from
tedious checking.”

**Good:** “`[Vaki25]` treats sheaf axioms, graded rings, and affine-cover
arguments in more detail than `[Hart10]`.”

A resource note should identify the work, its subject, and its relation to other
sources. Narrative about confusion, praise, reader effort, book length, or how
to use the book adds opinion and instructions while omitting bibliographic
information. Vague praise and claims that one text is better, clearer, or more
rigorous are not evidence. Replace each evaluative claim with a comparison that
names a checkable difference, or delete it.

### `RESOURCE-04`: Do not judge the reader’s competence or education

**Bad:** “A rigorous book for readers who failed to learn the subject
correctly.”

**Good:** “`[Shaf13]` covers [documented topics] in [cited sections].”

Resource prose must describe the work, not classify readers as deficient,
unprepared, forgetful, or properly educated. Claims such as “real proofs” also
disparage other sources without identifying a mathematical difference. This
language turns a bibliography into a judgment about the reader and makes a
recommendation depend on an invented personal history. State documented
coverage and source relations. Do not use a reader diagnosis as a reason to
choose a book.

### `RESOURCE-05`: Replace quality judgements with evidence

**Bad:** “The clearest and most rigorous introduction to the subject.”

**Good:** “The text defines [term], proves [theorem], and treats [topic] in
§§[locations].”

Words such as “clear”, “rigorous”, “complete”, “systematic”, and “accessible”
assert a quality without stating its measure. They make a resource annotation
sound authoritative while giving the reader no fact to check. Record contents,
theorems, sections, prerequisites, or a documented source relation instead.

### `RESOURCE-06`: Do not present ordinary textbook features as distinctions

**Bad:** “A book with proofs and a systematic treatment.”

**Good:** “The text proves [named theorem] after introducing [named hypotheses]
in §§[locations].”

Definitions, theorems, proofs, and an organized presentation are ordinary
features of a mathematics textbook. Mentioning them without a named scope or
location supplies no information and can imply that another text lacks them.
Describe the mathematical material that distinguishes the resource.

### `RESOURCE-07`: Keep comparisons professional and checkable

**Bad:** “This is the serious book; the other text leaves the real theory out.”

**Good:** “`[Shaf13]` treats [topic] in §§[locations]; `[Hart10]` treats
[different topic or section] in §§[locations].”

A comparison that ranks texts or assigns motives to their authors is opinion,
not bibliography. It can denigrate a source without identifying a difference
in mathematical coverage. Compare named topics, results, notation, sections,
or prerequisites, and omit status claims about books or readers.

### `RESOURCE-08`: Describe exposition without moral endorsements

**Bad:** “An unusually truthful introduction to the subject.”

**Good:** “The introduction discusses [named construction] through [named
examples].”

Calling an account honest, truthful, or candid gives it a moral endorsement
without identifying its mathematical contents. It also suggests that other
authors conceal or distort the subject. Describe the construction, explanation,
or examples that support the annotation. An actual error or omission requires
a specific statement and location, not a judgement about an author's integrity.

### `RESOURCE-09`: Replace vague explanatory promises with named content

**Bad:** “Explains what the theory is really about.”

**Good:** “Discusses generic points and nonreduced schemes.”

An explanatory promise with no named object, question, or result gives the
reader no way to identify the resource's scope. If a topic list follows, the
promise merely delays that information. State the topics directly. When the
annotation describes motivation, name the mathematical question or construction
being motivated. Use the example above only when the source covers those topics.

### `RESOURCE-10`: Describe scope without prescribing the reader's time

**Bad:** “Set aside a weekend for this chapter.”

**Good:** “The chapter covers [named topics].”

A resources page cannot assign a reader's schedule or decide how much attention
a text deserves. Such advice assumes priorities, background, and a purpose for
reading that the page does not know. State the scope and relevant locations so
readers can decide how the material fits their work. A verified page range
describes the document; it does not establish a reading duration.

### `RESOURCE-11`: Remove implied benchmarks for comprehension

**Bad:** “A prepared student can master this section in an afternoon.”

**Good:** Omit the performance claim. If prerequisites matter, name them:
“The section assumes familiarity with tensor products.”

A predicted completion time becomes an implicit standard of ability. Readers
who take longer can reasonably hear it as a judgement that they are slow or
inadequately prepared. It can also dismiss sustained study of the same material
in a course. Reading pace varies with purpose, depth, exercises, and prior
knowledge; elapsed time does not measure mathematical understanding. Remove
both numerical targets and substitutes such as “quickly”, “effortlessly”, or
“in one sitting” when they prescribe expected performance. Naming prerequisites
communicates mathematical dependencies without ranking readers. Verify those
prerequisites against the source.

### `RESOURCE-12`: State mathematical dependencies without diagnosing readers

**Bad:** “Confusion in geometry usually comes from weak algebra.”

**Good:** “For an affine scheme, the stalk at a prime ideal is the localization
of its coordinate ring at that prime.”

A broad diagnosis names neither the missing result nor the dependency that
would explain it. Frequency words such as “usually” add an empirical claim
without evidence. The sentence can also blame the reader's preparation for a
difficulty whose cause is unknown. State the particular objects, results, and
dependencies relevant to the page. Delete a general slogan when no such
connection is needed.

### `RESOURCE-13`: Name the mathematical outcome

**Bad:** “Turns combinatorial data into solutions.”

**Good:** “Constructs a toric variety from a fan.”

Words such as “answer”, “solution”, and “result” require an identified question
or operation. Without one, they conceal the resource's scope behind a promise
of usefulness. Name what is constructed, computed, proved, or classified, with
the relevant input and hypotheses. Use the replacement above only for a source
that covers that construction.

### `RESOURCE-14`: Remove unsupported rankings and implied consensus

**Bad:** “Remains the quickest reference for computations.”

**Good:** “Contains computations of [named invariant] in §[location].”

Superlatives require a comparison class and evidence. Claims about speed also
depend on the reader and the particular task. Words such as “still” and
“remains” can imply that a ranking has an established history without supplying
one. A resource inventory gains no mathematical information from this contest.
Describe the operation and its location; retain comparisons only when they
identify a verified difference relevant to the reader's question.

### `RESOURCE-15`: Describe distinctions without adversarial exam framing

**Bad:** “Explains the distinctions well enough to withstand an examiner's
challenge.”

**Good:** “Gives the implications among [named properties] and counterexamples
to their converses.”

Exam preparation does not make every mathematical description a claim about
performance under interrogation. Survival language makes the examiner an
adversary and replaces the actual distinction with an imagined test of the
reader. Qualifiers such as “well enough” also imply a threshold of adequacy
without stating it, and can disparage other treatments. Name the definitions,
implications, hypotheses, or counterexamples themselves.

### `RESOURCE-16`: Use direct bibliographic descriptions

**Bad:** “This volume is the home of the examples that settle the issue.”

**Good:** “Section [location] gives a [property A] example that is not
[property B].”

Conversational location metaphors make a book the supposed home of a subject
without identifying the relevant passage. Phrases such as “is where” and
“examples live” can also suggest exclusive ownership of material treated in
many sources. Use direct verbs such as “defines”, “treats”, or “contains”, and
name the content. Add a verified section reference when it helps locate the
material. Describe the example's mathematical role instead of promising that
it settles an unnamed issue.

### `RESOURCE-17`: Describe organization without prescribing reading methods

**Bad:** “Only dip into individual entries; reading the chapters consecutively
is a mistake.”

**Good:** “Entries are grouped by [documented subject headings].”

Readers choose a method according to their purpose and background. An annotation
cannot infer that sequential reading is inappropriate for them. Instructions
to browse or use an index also explain ordinary reading operations without
helping locate any material. Describe the actual organization or link the
relevant sections. Delete instructions that add neither content nor navigation.

### `RESOURCE-18`: Keep literature claims within the evidence

**Bad:** “No other source supplies these intermediate steps.”

**Good:** “Section [location] works through [named computation], including
[specific intermediate step].”

Knowing what one source contains does not establish what every other source
lacks. An unsuccessful search is evidence about that search, not proof of
absence from the literature. Describe the source's observable contents. Claims
of uniqueness or completeness require an explicitly bounded comparison and
evidence covering it. For a solution set, “complete” requires checking its
coverage against an identified course assignment or problem list.

### `RESOURCE-19`: Keep reputational judgements out of resource descriptions

**Bad:** “Student-authored notes in this area are generally unreliable.”

**Good:** “[Author], [title]: solutions to [identified exercises], [link].”

A resource directory identifies materials and supports navigation. Passing
judgement on authors or casting doubt on their work is outside that editorial
role. Supplying evidence does not make disparaging framing appropriate for a
study guide. Such framing can damage reputations, including those of graduate
students, while borrowing authority from the site's academic setting. Describe
contents and locations. A necessary mathematical correction belongs in a precise
erratum identifying the statement, version, and correction; do not turn it into
a verdict on a source or its author.

### `RESOURCE-20`: Distinguish access failures from properties of the work

**Bad:** “The abandoned notes have disappeared from the web.”

**Good:** Link an available copy under its author and title. Record a failed
address in an internal maintenance task when recovery work is needed.

A failed request establishes an access failure at a particular address and
time. It does not establish that the work is unavailable everywhere, abandoned,
or mathematically defective. Do not couple an access problem with a quality
judgement. Find a working source or archive location. An unnamed report of
unavailable materials gives the reader neither a resource nor a route to one.
Retain bibliographic information without a web link when it identifies a work
that readers can locate through a library or another concrete access route.

### `RESOURCE-21`: Build the resource directory before adding commentary

**Bad:** “There are many competing treatments, but few merit serious attention.”

**Good:** List identified works with author, title, citation, and access link;
group them under useful subject headings and annotate their documented scope.

A resource section serves retrieval and navigation. Readers need materials
they can identify, reach, and distinguish by content. General commentary about
the literature cannot substitute for those entries. Unsupported assessments
place the writer above other authors while withholding the evidence readers
would need to assess the claim. Supply the directory, topic links, section
locations, or source relations that make navigation useful. Use a hierarchy
when it helps readers locate material; do not add an introductory verdict on
the field in place of the resources themselves.

### `RESOURCE-22`: Read collective claims together with named resource lists

**Bad:** A paragraph dismisses a class of notes as poor scholarship, followed
elsewhere on the page by a list of authors of those notes.

**Good:** Introduce the list with its subject and scope, then give each work's
author, title, coverage, and link.

A collective judgement acquires identifiable targets through the surrounding
document. Separating the judgement from the names does not remove its
reputational effect. Readers can apply it to every listed author, even when the
writer never connects a particular name to the claim. Read introductions,
headings, annotations, and lists together. Remove the disparaging framing;
anonymizing the list or adding evidence does not repair its editorial purpose.

### `RESOURCE-23`: Do not prescribe permitted uses of worked solutions

**Bad:** “Read these worked examples only after solving the problems yourself.”

**Good:** “Worked solutions to [identified problems], with [documented topic]
computations in §[location].”

A resources page does not know whether the reader is checking a calculation,
studying a proof, comparing methods, or reviewing a topic. Restricting solutions
to answer checking assumes a single legitimate learning method and overrides
the reader's judgement. Describe what the solutions contain and which problems
they address. Leave the choice of use to the reader.

### `RESOURCE-24`: Do not frame learning from sources as harmful preparation

**Bad:** “Studying finished arguments undermines independent mathematical
thinking.”

**Good:** Omit the claim. Annotate the resource with its mathematical contents
and links to the corresponding problems.

This rhetoric invents a conflict between studying arguments and learning to
construct them. It dismisses a use of mathematical literature and presents an
unsupported theory of learning as an instruction. Invoking an oral exam does
not establish that causal claim or authorize judging the reader's preparation.
Keep source descriptions about the material. An exam's documented format can
be stated on its exam information page without using it to disparage resources
or police study methods.

### `RESOURCE-25`: Keep editorial authority within the page's purpose

**Bad:** “The discerning mathematician knows which treatments deserve study.”

**Good:** “The following sources cover [named topics].”

A study wiki serves mathematical exposition, reference, and navigation. Its
author does not thereby acquire authority to rank scholars, define competent
study habits, or speak for academic institutions. This is a question of
editorial role as well as evidence: even a defensible opinion can be misplaced
in a resource description. State mathematical content and source relations.
Remove language that positions the writer as an arbiter of readers' ability,
other authors' standing, or faculty expectations.

### `RESOURCE-26`: Do not invent faculty intentions or evaluation practices

**Bad:** “The committee will notice whether you have mastered these examples.”

**Good:** “The published syllabus lists [topic], [link to syllabus].”

Claims about what examiners know, infer from an application, or value in a
candidate presume access to their private reasoning. They also make the site
appear to speak on faculty members' behalf. State documented exam requirements
with attribution on the relevant exam page. A syllabus establishes its listed
scope; it does not establish an examiner's motives, attention, or judgement of
an individual candidate.

### `RESOURCE-27`: Replace competitive study priorities with dependencies

**Bad:** “Finishing the final chapter counts for more than working the earlier
problems.”

**Good:** “The proof of [result] uses [named earlier result].”

A ranking of study activities assumes the reader's goals, prior knowledge, and
assessment criteria. Invoking an examiner gives that prescription borrowed
authority without making it a mathematical dependency. Describe the specific
results used by later material. Do not turn chapter order or topic coverage
into a judgement about which study choices deserve credit.

### `RESOURCE-28`: Name applications without dismissing earlier material

**Bad:** “Only in the last part does the theory earn its keep.”

**Good:** “Chapter [location] applies [named theorem] to [named problem].”

A story in which earlier chapters merely accumulate machinery and later ones
justify it makes a sweeping value judgement about the subject. It supplies no
specific application and can dismiss independent reasons to study the earlier
material. Name the theorem, application, and location when that relation helps
the reader; omit the verdict on where the mathematics becomes worthwhile.

### `RESOURCE-29`: Treat public prose as speech attributed to the site owner

**Bad:** “We know what departments really expect from their candidates.”

**Good:** Attribute a documented requirement to the named department and link
its published description. Otherwise omit the assertion of institutional insight.

Readers attribute unqualified public statements to the site's owner. Agent-written
copy can therefore assign that person opinions, institutional authority, or
claims of insider knowledge they never expressed. This can misrepresent the
owner's professional relationships, especially when an early-career researcher
appears to lecture faculty or judge colleagues. Authorship assistance supplies
no mandate to invent a public persona. Keep claims within the page's purpose
and attribute institutional statements to their actual source.

### `RESOURCE-30`: Replace animated metaphors with the actual relation

**Bad:** “The definitions march into the chapter with examples at their side.”

**Good:** “The chapter introduces the definitions through examples.”

Giving mathematical objects entrances, companions, homes, or ambitions adds a
literary scene without specifying their mathematical or expository relation.
The resulting tone can resemble promotional copy rather than a reference work.
Use the verb that names the relation: a section contains examples, an author
introduces a construction, a proof uses a lemma, and a theorem implies a
conclusion. Grammatical agency alone is not a defect. These conventional verbs
are precise; replacing them with passive constructions is not required.
Established mathematical terminology and a metaphor that explains an actual
mathematical relation require separate judgement, not a blanket word ban.

### `RESOURCE-31`: Distinguish expository examples from historical motivation

**Bad:** “Each definition comes paired with the problem that originally
inspired it.”

**Good:** “The text introduces [named definition] through [named example].”

A source's choice of example does not establish the historical origin of a
definition. A definite phrase such as “the original problem” also presumes a
unique, identifiable origin. Describe how the text presents the material.
Attribute a historical motivation only when a source establishes that history.
Claims about every definition or construction require coverage of that whole
class; use a specific example when that is the evidence available. Do not
inflate an observed expository feature into a universal promise about the book.

### `RESOURCE-32`: Write as a contributor among peers

**Bad:** “We explain which authors deserve trust and how capable students study.”

**Good:** “The references below cover [topics], with links to [sections].”

Authorship of a study guide grants no authority over scholars' competence,
readers' learning, or faculty members' judgement. Mathematical expertise does
not supply knowledge of their individual circumstances or a mandate to rank
them. This boundary applies at every career stage. Write as a participant
contributing mathematics and references to a community. Describe sources and
mathematical relations without appointing the writer an evaluator of the
people who produce or use them.

### `RESOURCE-33`: Correct the assumed hierarchy, not just the adjective

**Bad:** “Only well-prepared readers will recognize the superior treatment.”

**Good:** “The treatment uses [method] to establish [result].”

Disrespect can result from the writer's assumed position without deliberate
hostility. Certifying authors, diagnosing students, directing readers, and
speaking for examiners all place the writer above the people described.
Polite wording, softer adjectives, or additional evidence leave that hierarchy
intact. Revise the function of the sentence: communicate mathematical content,
source coverage, or navigation. Assess the relationship the prose establishes
with readers and scholars, rather than guessing the writer's intentions.

### `RESOURCE-34`: Do not advertise proofs as certificates of author competence

**Bad:** “Unlike other accounts, this text supplies fully adequate proofs.”

**Good:** “The proof of [result] includes the calculation of [quantity].”

Presenting completeness or correctness as a resource's distinction makes an
ordinary mathematical obligation into an endorsement. It implicitly questions
whether other authors meet that obligation and appoints the annotator to
certify their work. The defect is this evaluative role, not merely missing
evidence or an inaccurate adjective. Describe the proof's method or the amount
of explanation where useful. Keep necessary corrections at the level of the
particular mathematical statement, as in `RESOURCE-19`.

### `RESOURCE-35`: Use expository modifiers with professional restraint

**Bad:** “The only satisfactory account of the argument.”

**Good:** “The text gives a detailed calculation of [quantity].”

Modifiers such as “short”, “long”, “detailed”, and “terse” can describe the
presentation without passing judgement on an author's mathematical competence.
This vocabulary permits useful distinctions while maintaining professional
respect. Choose the modifier for a specific, observed feature; it is not a
stock compliment or a ranking. A terse proof can establish its conclusion,
and additional detail does not by itself establish correctness. Do not replace
a description of exposition with a verdict on adequacy, honesty, or scholarly
standing. Omit the modifier when the named content already supplies the useful
information.

### `RESOURCE-36`: Describe mathematical work without imposing preferences

**Bad:** “The proposition spares readers the tiresome local calculations.”

**Good:** “The proposition reduces [specified verification] to [specified
affine-local conditions].”

Calling proofs tedious, unrewarding, or a chore presents a personal dislike as
a property of the mathematics. Readers may enjoy those arguments or learn from
working through them. The judgement implicitly dismisses that interest and
makes avoiding the work seem preferable without explaining the mathematical
reduction. State what a result proves or what verification it reduces. Keep
preferences about the experience of doing mathematics out of resource copy.

### `RESOURCE-37`: Bound exam-frequency statements to recorded observations

**Bad:** “Examiners generally start with the classical material.”

**Good:** Report a table of observed opening-question topics, counts, and the
identified exam records, institutions, and dates from which they were obtained.

A claim about exam frequency can be useful when the repository's records
support it. It cannot come from the annotator's assumed knowledge of faculty
practice. Identify the observed population, denominator, counting unit, and
source records. Distinguish recorded opening questions from questions appearing
elsewhere in an exam; total topic counts cannot establish how exams begin.
Disclose incomplete records and avoid extrapolating a local sample to other
examiners or institutions. Classify questions by reading their mathematics.
Evidence about frequency does not by itself prescribe a student's priorities.

### `RESOURCE-38`: Prefer ordinary descriptions to editorial labels

**Bad:** “An illustration-driven presentation with the ideal pedagogical mix.”

**Good:** “Has many examples.”

An ordinary feature rarely needs a coined label, a verdict on its instructional
balance, or an imagined exam scenario. Those additions increase the reading
cost without identifying more content. Use familiar words for the observed
feature. If a specific example matters, name it and its location instead of
adding praise. Do not replace bloated prose with a compressed label that still
sounds promotional or requires interpretation.

### `RESOURCE-39`: Organize topic lists around a useful relation

**Bad:** “Geometry, a worked intersection, derived functors, and an illuminating
picture.”

**Good:** Group source links under a named topic, with section locations and a
brief description of each section's contribution.

A list of mathematical terms is not a synthesis merely because the terms are
technical. Mixing whole subjects, individual constructions, examples, and vague
visual descriptions leaves the reader to reconstruct their relation. Choose
the scope and grouping for a navigational purpose. Use a broad subject label
for broad coverage, or identify precise sections for particular topics. A list
earns its length through useful selection, organization, and locations, not
through the appearance of mathematical density.

### `RESOURCE-40`: Supply resource navigation as the substantive deliverable

**Bad:** An essay ranks books and sketches their personalities while leaving
readers to find their contents and relevant sections.

**Good:** A topic index connects identified exam topics to sources, chapters,
sections, exercises, and recorded questions, with working links.

The resource section should reduce bibliographic work that students would
otherwise repeat. Collect and organize available tables of contents, locate
specific topics, and connect relevant source passages and problems. Preserve
source identities and locators so readers can inspect the relations. Build a
navigable hierarchy where it helps retrieval. Make each mapping through reading
the source material; a plausible topic list is not a substitute for curation.
The result should let readers spend their attention on mathematics rather than
reconstructing the bibliography.

### `RESOURCE-41`: Do not confuse neutral wording with completed curation

**Bad:** Replace a book-ranking paragraph with “Several sources discuss this
subject” and leave the resource entries unlocated and unorganized.

**Good:** Provide the identified works, their access links, and the section
references needed for the page's topics.

Removing conceited commentary repairs the tone but does not supply missing
reference work. A resource page remains incomplete when readers must perform
the searches and cross-referencing it exists to provide. Judge the result by
whether a reader can locate the relevant material. Concise prose supports that
function; it cannot replace the source reading and organization needed to
deliver it.

## Precision policies

These policies prevent prose from taking the place of a typed mathematical
statement. The general reason is the same in each case: a reader must be able
to identify the objects, maps, hypotheses, and conclusion without guessing.

### `PRECISION-01`: Replace mood words with definitions

**Bad:** “A scheme is a geometrically complete space.”

**Good:** “A scheme is a locally ringed space locally isomorphic to the spectrum
of a commutative ring.”

Vibe adjectives sound technical while leaving the defining conditions unknown.
Use the standard term and state its definition.

### `PRECISION-02`: Replace vague qualifiers with exact scope

**Bad:** “This holds essentially for finite type schemes.”

**Good:** “This holds for schemes locally of finite type over a field.”

Words such as “essentially”, “basically”, “morally”, and “in some sense” hide
the hypothesis or weaken a claim without saying how. State the exact scope, or
name a genuine approximation such as “up to isomorphism”.

### `PRECISION-03`: Name operations instead of using empty collective nouns

**Bad:** “The construction carries the required structure.”

**Good:** “The pullback sheaf has restriction maps satisfying the sheaf axiom.”

“Data”, “structure”, “property”, “framework”, “package”, and “setting” are
acceptable only when they have a fixed mathematical referent. Otherwise they
hide the operations or axioms the reader must check.

### `PRECISION-04`: State universal constructions as universal constructions

**Bad:** “Define $E\to X$ by pulling back $U\to B$ along $X\to B$.”

**Good:** “Let $E$ be the pullback in the Cartesian square
$E\to U$, $E\to X$, $U\to B$, $X\to B$.”

“Obtained by pulling back” is an instruction without the square, maps, or
universal property. Give the diagram or state the property that characterizes
the object.

### `PRECISION-05`: Bind symbols before using them

**Bad:** “The map $f$ is surjective, where $X$ is the source.”

**Good:** “For schemes $X$ and $Y$, let $f\colon X\to Y$ be a morphism. Assume
$f$ is surjective.”

An unbound symbol forces the reader to recover its type and scope from later
prose. Introduce every object, map, index, and codomain before its first use.

### `PRECISION-06`: Give every map its domain and codomain

**Bad:** “Consider the natural map $f$.”

**Good:** “Consider the natural morphism $f\colon X\to Y$ induced by the ring
map $A\to B$.”

A map without its source, target, and construction cannot be checked or composed.
The type is part of the mathematical statement.

### `PRECISION-07`: Use standard terms and notation

**Bad:** “The value space of $M$” when the object is an $R$-module $W$.

**Good:** “Let $b\colon M\otimes_R M\to W$ be a $W$-valued bilinear form.”

Invented terms and elegant variations make readers guess whether a new object
was introduced. Use the standard name, or define the new term before using it.

## Structure policies

These policies protect the logical skeleton of the book. A section or example
must carry a mathematical unit that a reader can identify and reuse.

### `STRUCTURE-01`: Give each definition one defining occurrence

**Bad:** Define “scheme” in a lede, restate it in a remark, and use both
versions as if they had equal authority.

**Good:** Give one fenced definition, then link to it and state consequences
where they are used.

Multiple defining occurrences drift apart and make it unclear which hypotheses
govern later claims. One defining occurrence gives the term a stable referent.

### `STRUCTURE-02`: Put a primary mathematical unit in every section

**Bad:** A section contains only “This is useful for the next chapter” and a
list of links.

**Good:** Give the section a definition, theorem, example, counterexample, or
worked calculation, then use remarks and links to support it.

Without a primary unit, a section is navigation or process prose disguised as
exposition. Secondary remarks cannot carry the chapter's logical skeleton.

### `STRUCTURE-03`: Keep examples subordinate to the definition they illustrate

**Bad:** “Affine space is an important example of a scheme.”

**Good:** “For a ring $A$, the locally ringed space $\operatorname{Spec}(A)$ is
an affine scheme. When $A=k[x_1,\ldots,x_n]$, it is affine $n$-space over
$k$.”

An example should instantiate the defining data. Calling something an example
without showing the instance gives the reader no mathematical test.

### `STRUCTURE-04`: State propositions as propositions

**Bad:** “The following is the key fact about proper morphisms.”

**Good:** “A proper morphism of schemes is universally closed, separated, and
of finite type.”

Labels such as “key fact” and “important result” announce status instead of
stating a claim. Name the hypotheses and conclusion so the reader can apply it.

### `STRUCTURE-05`: Use references for mathematical referents

**Bad:** “As discussed above, this map is an isomorphism.”

**Good:** “By the normalization theorem, the induced map is an
isomorphism.”

Position and memory are unstable references. Link the named theorem, card, or
page when the reader must use it.

### `STRUCTURE-06`: Use parentheticals only for genuine qualifications

**Bad:** “The map is finite (and this is important, as we will see below).”

**Good:** “The map is finite (equivalently, the target coordinate ring is a
finite module over the source coordinate ring).”

Parentheticals should restrict or identify the claim. If they only announce
future explanation, motivation, or emphasis, move the mathematical content into
the main sentence or delete the parenthetical.

## General mathematical authoring policies

These policies govern contributor-authored mathematical exposition: wiki
chapters, guides, definition and theorem cards, solutions, hints, and remarks.
They are the detailed source for the concise rules above. They govern
structure, exposition style, level of detail and rigour, uniform presentation,
completeness, and linking. They do not govern a problem's statement, which
keeps its source's wording, notation, and conventions under `QUAL-01`, and they
do not prescribe which definition, generality, or foundations the exposition
adopts: that mathematics comes from the textbooks and notes the corpus draws
on.

## Prose (`PR-*`)

Bad prose on its own terms. The fix is a rewrite.

### `PR-1`: Self-narration

The prose describes what the document is or does instead of doing it.

**Banned:** "This section is the framework for everything that follows; it is
mathematics, not bookkeeping."

**Preferred:** "The fundamental group of the circle is $\mathbb Z$, generated
by the class of the loop $t\mapsto e^{2\pi it}$." State the content; do not
characterize the text.

### `PR-2`: Reflexive negative parallelism

A notion is characterized by contrast with the alternative it rejects:
"X, not Y" / "is X, never Y" / "not just X but Y" / "X rather than Y"
— including manufactured negative parallelism of the form "their mere
existence supplies no $X$," which negates an expectation no one held.
Existence of objects never supplies an order, a comparison, or extra
structure unless one is defined; stating that it does not is true by
default and adds no claim to the skeleton (SEC-6). The contrast sounds
substantive while carrying no content, and it wastes the reader's
attention on a strawman.

**Banned:** "$a = b$ is a theorem, never a definitional identity";
"Their mere existence supplies no order relation among them" — when
several targets are available, the comparison data are either a chosen
target or a functor comparing the targets; that existence alone supplies
no order is the default and states nothing.

**Preferred:** state the positive claim and stop. "When several targets
are available, the comparison data are either a chosen target or a
functor comparing the targets." If the contrast carries information
(e.g. a genuine non-example where an expected order fails), make it a
Remark and explain the precise obstruction in context.

### `PR-3`: Self-certification

The text asserts it satisfies a property — dependency order, completeness,
minimality, "the single source", "canonical", "self-contained" — which no
sentence can make true.

**Banned:** "The definitions and results, in dependency order."

**Preferred:** delete the assertion. If the property is required, record it
where an auditor checks it against the artifact.

### `PR-4`: Theory of mind

The prose tells the reader what the mathematics implies or how to read it.

**Banned:** "equality, isomorphism, and equivalence are distinguished and
named wherever the distinction is content."

**Preferred:** delete. Distinct definitions are already distinct.

### `PR-5`: Puffery and AI-vocabulary

Words that rate the mathematics or belong to the generic LLM register.

**Banned:** "crucial", "pivotal", "powerful", "elegant", "deep", "rich",
"intricate", "interplay", "robust", "seamless", "leverage", "delve",
"underscore", "showcase", "boasts", "foster", "meticulous", "tapestry",
"testament", "landscape", "realm", and the connectives "it is worth noting",
"importantly", "note that", "of course", "clearly" (where it is not).

**Preferred:** delete the word; state the content plainly.

### `PR-6`: Cadence padding

Structure produced for rhythm.

**Banned:** the reflexive rule of three, "not only … but also", formulaic
transitions opening successive sentences ("Additionally", "Moreover",
"Furthermore", "Notably"), conclusion-restatement ("in summary", "as we have
seen"), em-dash or parenthetical density.

**Preferred:** keep what is needed; cut what is there for cadence.

### `PR-7`: Concept defined by notational payoff

A theorem or property is characterized by its effect on notation rather than
by its mathematical content, using a conversational construction ("is what
licenses", "is what allows", "is what lets us") instead of stating the
theorem and deriving the convention from it.

**Banned:** "Coherence is what licenses the notation
$a_1\otimes\cdots\otimes a_n$ without parentheses."

**Preferred:** "By the coherence theorem, any two parenthesizations of
$a_1 \otimes \cdots \otimes a_n$ are connected by a unique composite of
associators, so the expression is independent of parenthesization;
parentheses are omitted." State the theorem — what is well-defined, and in
what sense — then let the notational convention follow as a consequence.
A standard text may explain that a theorem permits a notational shorthand;
it does not define the theorem as that shorthand's justification.

### `PR-8`: Superficial "-ing" analysis

A trailing participial clause performs analysis without adding content.

**Banned:** "the pullback is universal, underscoring the classifier's role."

**Preferred:** delete the clause, or replace it with the statement it gestures
at — a theorem, a cross-reference, an actual consequence.

### `PR-9`: Construction and verification in one sentence

A single sentence simultaneously constructs an object and verifies its
required properties, hiding the logical structure the reader needs to follow.

**Banned:** "A category with finite products is monoidal with
$a\otimes b$ a chosen product $a\times b$ and $e$ a terminal object, the
three isomorphisms being the unique ones commuting with the projections; this
is the cartesian monoidal structure."

**Preferred:** separate the construction from the verification. "The product
functor $\times\colon\mathcal{C}\times\mathcal{C}\to\mathcal{C}$, together
with a terminal object $\mathbf{1}$ as unit, defines a monoidal structure
on $\mathcal{C}$. The associator $\alpha_{a,b,c}$ and the unitors
$\lambda_a$, $\varrho_a$ are the unique isomorphisms supplied by the
universal property of the product." State the functor, then verify the
axioms. A reader follows construction, then verification; a semicolon-joined
sentence conflates them.

### `PR-10`: Undue emphasis

`**bold**` or `*italic*` used to weight a clause, or to mark a defined term in
running prose.

**Preferred:** mark a term at its definition only with `\dfn{term}`
(`DEF-26`); use **bold** only as a run-in label at the start of a list item or
paragraph ("**In $\mathbf{Set}$.**", "**Remark.**"). Never use emphasis to
weight a clause.

### `PR-11`: Formatting tells

**Banned:** Title Case in headings; curly quotes; emoji; collaborative or
meta language ("let me know", "I hope this helps"); bold-header bullet lists
where prose is clearer.

**Preferred:** sentence case in headings; straight quotes; no emoji; no
collaborative or meta language.

### `PR-12`: Project process inside mathematical exposition

A mathematical page pauses to discuss rulings, audit procedure,
implementation status, or editorial policy.

**Banned:** "This ruling guards the conversion pipeline and is enforced by
the audit."

**Preferred:** state the mathematical proposition. Project process belongs in
[COMPLAINTS.md](COMPLAINTS.md) and [TODO.md](TODO.md) (`QUAL-08`), not on a
mathematical page.

## Evasion (`EV-*`)

Prose that substitutes for mathematical work not done. The tell is stylistic;
the defect is that a definition was not written or an object not named. The
remediation is never a nicer phrase — it is the work.

### `EV-1`: Vibe-adjectives for a definition

Impressive qualifiers replace the definition itself.

**Banned:** "The subcategory is structurally complete under sameness."

**Preferred:** write the definition —
`A full subcategory $\mathcal D\subseteq\mathcal C$ is \dfn{replete} if every object of $\mathcal C$ isomorphic to an object of $\mathcal D$ belongs to $\mathcal D$.`
"Structurally complete under sameness" is a mood; the definition is the work.

### `EV-3`: Engineering collective nouns

"package", "frame", "pipeline", "suite", "layer", and a vague "slice" gather
mathematical objects under a process or software noun instead of naming them.

**Banned:** "the discriminant package"; "the forms frame"; "the equality
slice".

**Preferred:** "the discriminant construction and its exact sequences"; "the
categories $\mathcal B_{R,W}$ and $\mathcal Q_{R,W}$"; the exact chapter,
section, or mathematical construction meant.

### `EV-4`: Vague hedges for precision

**Banned:** "essentially", "basically", "morally", "roughly", "in some sense"
used where an exact statement is owed.

**Preferred:** state it exactly, or, if a genuine approximation is meant,
name the sense ("up to isomorphism", "to first order").

### `EV-8`: Universal property invoked but not stated

A sentence appeals to "the projections", "the universal property", or "the
unique map" without stating which universal property, from which object, to
which target. The uniqueness is real, but the reader cannot verify it
without the property identified.

**Banned:** "the three isomorphisms being the unique ones commuting with the
projections."

**Preferred:** "the associator $\alpha_{a,b,c}$ and the unitors
$\lambda_a$, $\varrho_a$ are the unique isomorphisms supplied by the
universal property of the product." Name the universal property and the
object that supplies it.

## Mathematical tells (`MA-*`)

Colloquial or reinvented parlance in place of the standard notion, or of the
definition the corpus already fixes on a definition card. The remediation is
the established definition — link it.

### `MA-1`: Prior substitution for the corpus's definition

An agent writes the definition it recalls from training or an external source
without reading the definition card the corpus already has for the notion.

**Banned:** calling a space compact in the sense of sequential compactness on
a page whose linked definition card defines compactness by open covers.

**Preferred:** read and link the corpus's definition card. If that card
conflicts with the literature, correct the card and repair the pages that
depend on it; do not shadow it locally.

### `MA-2`: Coinage for a standard notion

A private word stands in for a notion with a standard name.

**Banned:** "blow-up point" for a pole; "wrap number" for the winding number;
"refinement" for a full subcategory.

**Preferred:** the standard term, as the corpus's definition card names it.

### `MA-3`: Notation colliding with a standard meaning

A symbol is reused against its near-universal reading.

**Banned:** "$\mathbf{Sh}_\Sigma$" for a diagram/functor category ("$\mathbf{Sh}$"
is sheaves).

**Preferred:** a non-colliding symbol ("$\mathbf{Dia}_\Sigma$"), or the plain
construction ($\operatorname{Fun}(\Sigma, \mathcal C)$).

### `MA-4`: Elegant variation

The same object is renamed sentence to sentence to avoid repetition, so one
notion acquires several names.

**Preferred:** repeat the exact term. Notation keeps its meaning throughout a
page and across the corpus's authored exposition.

### `MA-5`: Borrowed technical term without a definition

A word that carries a specific technical meaning (character, spectrum, kernel,
index, module, classified by) is used loosely to describe something that has
a different, standard name. A mathematician reads it as the technical term
and finds no matching definition — the word signals precision and delivers
none.

**Banned:** "the character of an axiom" (read as a group/representation
character; no such notion is defined); "the bilinear map classified by
$\mu$" (classified by means a classifying object represents a functor;
the correspondence is the tensor-hom adjunction).

**Preferred:** state the actual correspondence or property. "The bilinear
map $A\times A\to A$ corresponding to $\mu$ under the tensor-hom
adjunction." Use the standard name for the standard notion.

### `MA-6`: Cardinality label for an incidental count

Naming a structure by how many things it has — "trichotomy", "dichotomy", "the
three-fold", "$N$-fold" — asserts the count is mathematically load-bearing.

**Banned:** "the stuff / structure / property trichotomy" — nothing turns on
"three".

**Preferred:** name the classification by content, not by tally.

### `MA-7`: Backwards or premature notation

A symbol is introduced with `:=` pointing from the standard notation to a
coinage, or coined notation is used before it is defined.

**Banned:** "$E_A := B_A.A$" before either notation has a defining occurrence.

**Preferred:** define each object first; only afterward introduce a shorthand,
with `:=` pointing from the new symbol to the defined expression.

### `MA-9`: Colloquial "ownership" for a mathematical relation

"owns", "owned at", and "ownership" replace the relation that should be
stated.

**Banned:** "commutativity is owned at $\mathbf{Mag}$"; "the node that owns
the property"; "the object owns its local invariants".

**Preferred:** name the relation — "commutativity is a property of magmas",
"the category whose objects satisfy the property", "the invariants are
defined on the object".

### `MA-12`: Named maps referred to by count

Standard maps with standard names — the associator $\alpha$, the left unitor
$\lambda$, the right unitor $\varrho$ — are referred to as "the three
isomorphisms" or "the $n$ maps" instead of by name. The reader must infer
which maps from context.

**Banned:** "the three isomorphisms being the unique ones commuting with the
projections."

**Preferred:** "the associator $\alpha_{a,b,c}$ and the unitors
$\lambda_a$, $\varrho_a$." Name the maps. The count carries no mathematical
information.

## Definitions (`DEF-*`)

### `DEF-1`: One defining occurrence

Each mathematical notion has one defining occurrence in the corpus: its
definition card (`D-…`). Wiki pages, guides, and solutions link or transclude
that card. They do not restate it, shadow it with a synonym, or write a second
local definition. A card that records a source's variant of a definition
carries a `variant-of` relation to the card the wiki uses.

### `DEF-2`: Read the definition card before writing a dependent passage

Read the corpus's definition card, and the cards it links, before writing a
passage that depends on the notion. A definition reconstructed from training
or an external source is inadmissible even when it resembles a standard
definition.

### `DEF-3`: Correct at the defining occurrence

If a definition card conflicts with the literature, correct the card and
repair the pages that depend on it. Do not shadow it locally.

### `DEF-4`: Definition block syntax

A definition is a `::: {.definition}` block on a definition card. The card's
front matter supplies its `id`, `title`, and classification; the block states
the definition, with the definiendum marked by `\dfn` (`DEF-26`).

```markdown
::: {.definition}
A family $\mathcal F$ of holomorphic functions on an open set $\Omega$ is
\dfn{normal} if every sequence in $\mathcal F$ has a subsequence that converges
uniformly on compact subsets of $\Omega$.
:::
```

## Cross-references (`XREF-*`)

### `XREF-1`: Link cards by ID

A reference to a definition, theorem, or problem is a wikilink to its card ID:
`[[D-IJMPJ]]`, or `[[D-IJMPJ|normal family]]` to set the link text inside a
sentence. A paragraph that holds nothing but card links transcludes those
cards in place. Card IDs are stable; a reference by position ("above", "the
previous theorem") is not.

### `XREF-4`: Pages and sections

Link a wiki page by its path and a section of it by its heading, with link
text that reads as part of the sentence:
`[[calculus-preliminaries#Green's Theorem|Green's theorem]]`.

## Citations (`CITE-*`)

### `CITE-1`: Better BibTeX keys

Use Better BibTeX keys: `[@OR23, Definition 1.5.1]`. Zotero is the source of
truth. If a work is not in Zotero, add it there first.

### `CITE-2`: No inline URLs

**Banned:** an inline URL to arXiv, a DOI, or nLab.

## Diagrams (`DIA-*`)

### `DIA-2`: Every arrow is labeled

Every arrow in an authored diagram is labeled with the map it denotes, and its
source and target are the displayed objects. Membership of an object in a
category is not drawn as an arrow between categories.

## Notation (`NOT-*`)

### `NOT-1`: State the mathematical type

State the mathematical type of every named entity: whether a symbol denotes an
element, a set, a map, a space, a group, a ring, a module, a category, or a
functor, and where it lives.

### `NOT-2`: Distinct symbols for equality and isomorphism

Literal equality ($=$), isomorphism ($\cong$), and equivalence ($\simeq$) are
written with distinct symbols. An isomorphism is not written as an equality.

### `NOT-3`: One symbol, one meaning

A symbol has the same meaning throughout a page and across the cards it
transcludes. Nonstandard notation is introduced at its defining occurrence,
after the standard construction it abbreviates has been stated. A problem
statement keeps its source's notation (`QUAL-01`).

### `NOT-4`: Standard names

Use established names in their standard meanings, as the corpus's definition
cards give them. Do not coin a name for a notion that already has one
(`MA-2`).

## Properties and structure (`STR-*`)

### `STR-2`: Name every chosen structure

When an object carries more than one standard structure, name the one a
construction uses. Tensor product and direct sum give different monoidal
structures on modules; a ring is a group under addition, not under
multiplication.

### `STR-3`: State every hypothesis

A theorem states every object property, characteristic restriction, limit
assumption, flatness assumption, and equality of named morphisms used in its
conclusion. If a construction uses a basis, embedding, section, presentation,
or other witness, name that witness in the construction.

## Examples and presentation (`EX-*`)

### `EX-1`: An example mirrors the definition's form

An example instantiates each slot of the structure it exemplifies. If a
monoidal category was defined as a tuple
$(\mathcal{C}, \otimes, \mathbf{1}, \alpha, \lambda, \varrho)$, the example
presents the tuple: "Let $\mathcal{C}$ be a category with finite products
and terminal object $e$. Then $(\mathcal{C}, \times, e)$ is a monoidal
category." The reader who just read the definition sees which slot is
which without parsing prose. Listing the components in a sentence instead
of presenting the tuple is readable but does not mirror the definition's
grammar.

**Banned:** "A category with finite products is monoidal with $a\otimes b$ a
chosen product $a\times b$ and $e$ a terminal object, the three isomorphisms
being the unique ones commuting with the projections; this is the cartesian
monoidal structure."

**Preferred:** "Let $\mathcal{C}$ be a category with finite products and
terminal object $e$. Then $(\mathcal{C}, \times, e)$ is a monoidal category,
with associator and unitors the canonical isomorphisms supplied by the
universal property of the product."

### `EX-2`: An example is an example, not a proposition

If there is nothing to prove, do not present the passage as a proposition
with a proof. A category with finite products is an example of a monoidal
category, not a theorem. Put it in a `::: {.example}` block, and reserve
`::: {.proposition}` blocks and proofs for statements that require
verification beyond unpacking the definition.

## Axioms and definitions (`AX-*`)

### `AX-1`: A definition that names axioms without stating them

A definition must fully determine the notion it introduces. Referencing
axioms by name — "satisfying the two hexagon conditions", "satisfying the
pentagon axiom" — without stating or drawing the diagrams is not a
definition. The reader cannot evaluate whether a given object satisfies the
definition, because the name of an axiom is not the axiom. State the
equations or draw the diagrams. If they are long, cite the exact diagrams
by reference to where they are written in full.

**Banned:** "A braiding on a monoidal category is a natural isomorphism
$\gamma_{a,b}\colon a\otimes b\cong b\otimes a$ satisfying the two hexagon
conditions relating $\gamma$ to $\alpha$."

**Preferred:** state or draw both hexagon diagrams. The definition names
each component and each axiom; the axioms are commutative diagrams, and a
definition either draws them or cites the exact reference where they are
written.

### `AX-2`: An axiom described by shape instead of by equation

"The hexagon conditions", "the pentagon axiom", "the triangle identities" —
the shape name is a mnemonic, not a mathematical condition. The condition
is a commutative diagram or an equation. Use the shape name alongside the
diagram, not in place of it. A reader who does not already know the shape
cannot reconstruct the axiom from its name.

**Banned:** "satisfying the two hexagon conditions relating $\gamma$ to
$\alpha$."

**Preferred:** draw the two hexagon diagrams, or write the equations they
commute. The name "hexagon" may appear as a label; it may not substitute
for the diagram.

### `AX-3`: "relating" an axiom to its components without stating the relation

"relating $\gamma$ to $\alpha$", "commuting with the projections",
"compatible with the tensor product" — each names a relationship without
stating the equation or diagram that expresses it. A definition or theorem
that invokes a relation states the relation: the commutative diagram, the
equation, or the naturality square. "Relating" and "compatible" gesture at
a mathematical statement that is not written.

**Banned:** "satisfying the two hexagon conditions relating $\gamma$ to
$\alpha$."

**Preferred:** state the relation — the hexagon diagrams express that
specific composites of $\gamma$, $\alpha$, and the tensor product's
functoriality are equal. Draw the diagrams or write the equations.

### `AX-4`: A definition that is not self-contained

A definition must be evaluable from the text plus its cited references. A
definition that references axioms by name without stating them and without
citing where they are written in full gives the reader neither the axioms
nor a pointer. The reader cannot determine whether a given object satisfies
the definition. Self-contained does not mean everything is derived from
first principles in one sentence — it means the text or its cited
references supply every component the definition requires.

**Banned:** "A braiding on a monoidal category is a natural isomorphism
$\gamma_{a,b}\colon a\otimes b\cong b\otimes a$ satisfying the two hexagon
conditions relating $\gamma$ to $\alpha$." No diagrams, no citation.

**Preferred:** draw the hexagon diagrams in the definition, or write
"[@MacLane, Chapter VII, (2.1) and (2.2)]" citing the exact diagrams. The
reader follows the citation and finds the axioms; or the reader reads the
diagrams in the text. Either way the definition is evaluable.

### `AX-5`: An axiom named by count without stating or citing the axioms

"The two hexagon conditions", "the three coherence axioms", "the five
simplicial identities" — a count of axioms without stating or citing them
combines AX-1 and AX-2 with a cardinality label. The count tells the reader
how many axioms to imagine without supplying them. Name each axiom, draw
each diagram, or cite the exact reference for all of them. The count is not
a substitute.

**Banned:** "satisfying the two hexagon conditions."

**Preferred:** draw both hexagon diagrams, or cite the reference where both
are written. The reader does not need to be told there are two; the reader
needs to see them.

## Terminology (`TERM-*`)

Use established mathematical terms in their standard meanings. Do not coin a
name for a notion that already has one. Do not import a term from another
field where a standard mathematical term exists. Do not overload a standard
word with a project-management or implementation meaning.

Terminology failures have three recurring forms:

- **Foreign-discipline substitution.** A technical term from another field is
  used where the exposition owes a standard mathematical term and its
  definition.
- **Project coinage.** An undefined word is made to do mathematical work.
- **Colliding overload.** A standard word such as "kernel", "core", or
  "fiber" is reused with a project-management or implementation meaning.

## Parentheticals (`PAR-*`)

A semantic parenthetical is a compression. Prefer expansion over compression:
expanding into explicit mathematics is reversible, whereas a compression is
lossy and usually smuggles an undefined term or an unstated theorem.

### `PAR-1`: Compression artifact

Terse to the point of inscrutability, standing in for a notion that needs
spelling out.

**Banned:** "weak homotopy equivalence (holds; inverts/ignores
directionality) versus categorical equivalence (fails; preserves it)."

**Preferred:** expand into prose or a definition that states the
distinction.

### `PAR-2`: Smuggled theorem or equivalence

"(equivalently, $X$)", an "iff" asserted in a parenthesis, often over
undefined terms.

**Banned:** "full and faithful (equivalently, a replete full subcategory)"
— a functor is identified with its essential image and an equivalence is
asserted aside.

**Preferred:** "If $F\colon\mathcal C\to\mathcal D$ is fully faithful, then
$F$ induces an equivalence from $\mathcal C$ to its replete full essential
image in $\mathcal D$." Cite the result and define any term not already
established. The expanded statement can later be demoted to a remark, cited
theorem, or footnote.

### `PAR-3`: Smuggled example

"(e.g. …)" carrying a genuine example.

**Banned:** "several distinct lifts (e.g. several monoidal structures on one
category)."

**Preferred:** promote to a first-class example block.

### `PAR-4`: Legitimate qualification

A small, correct, load-bearing modifier. Keep inline.

**Fine as is:** "fibers are (possibly nontrivial) groupoids."

### `PAR-5`: Padding or tangent

Carries no load.

**Preferred:** delete. A parenthetical is usually wrong when it is a
tangent.

## Not flags

Standard mathematical hedging and signposting that carry real content are not
violations: "provided", "up to isomorphism", "without loss of generality", a
genuine sign or normalization convention, and a Remark that explains a real
subtlety in context. The test is whether removing the phrase removes
information. A tagline removes none.

## Symbols and binding (`SYM-*`)

Mathematical text follows scoping and binding conventions analogous to those
in a formal language. A symbol is bound at the point where the object it
names is declared — with its type, domain, codomain, or constituent data.
Before that point, the symbol is unbound and the reader cannot determine
what it refers to. Naming a type ("let $\mathcal{C}$ be a monoidal
category") does not bind the symbols for that type's constituent data
($\otimes$, $\mathbf{1}$, $\alpha$, $\lambda$, $\varrho$); those are bound
by stating the tuple
$(\mathcal{C},\otimes,\mathbf{1},\alpha,\lambda,\varrho)$. A symbol used
before its binding is an unbound reference; a symbol that changes meaning
within a passage is a shadowing conflict.

### `SYM-1`: A symbol used without being bound

A passage uses a symbol before declaring the object it names. No type, no
domain, no codomain, and no constituent tuple is stated. The reader cannot
determine what the symbol refers to without external knowledge. Bind the
symbol first: state the object, its type, and the map's domain and
codomain (or the structure's tuple). Then use the symbol.

**Banned:** "A monoid in $(\mathbf{Ab},\otimes_{\mathbb Z},\mathbb Z)$ is a
ring, its multiplication being the bilinear map classified by $\mu$ and its
unit the image of $1$ under $\eta$." The symbols $\mu$ and $\eta$ are used
without being introduced; no abelian group $A$ is named; no domains or
codomains are stated.

**Banned:** "Let $S$ be a symmetric monoidal category. … Then $\otimes$
makes $S^{\mathrm{iso}}$ an abelian monoid." The tensor $\otimes$ is used
without being bound — stating the type "symmetric monoidal category" does
not introduce the symbol $\otimes$.

**Preferred:** "A monoid object in
$(\mathbf{Ab},\otimes_{\mathbb{Z}},\mathbb{Z})$ is a triple
$(A,\mu,\eta)$ where $A$ is an abelian group,
$\mu\colon A\otimes_{\mathbb{Z}}A\to A$ is a homomorphism, and
$\eta\colon\mathbb{Z}\to A$ is a homomorphism. The bilinear multiplication
$A\times A\to A$ is the map corresponding to $\mu$ under the tensor-hom
adjunction, and the unit element is $\eta(1)$." Name the data, then use the
symbols.

### `SYM-2`: Data referenced by role instead of by declaration

A passage refers to "the multiplication", "the unit", "the associator", or
"the classifying map" without first declaring the object that plays that
role. The role name presupposes the data without stating it. Declare the
data — the map, its domain, its codomain — then refer to it by name. A role
description is a comment on data that has been stated, not a substitute for
stating it.

**Banned:** "its multiplication being the bilinear map classified by $\mu$"
— "the multiplication" is a role; $\mu$ is undeclared; "the bilinear map
classified by $\mu$" describes what $\mu$ does without stating what $\mu$
is.

**Preferred:** "$\mu\colon A\otimes_{\mathbb{Z}}A\to A$ is a homomorphism;
the corresponding bilinear map $A\times A\to A$ is the multiplication."
Declare the map, then name its role.

### `SYM-4`: A symbol overloaded within one passage

A single symbol is used for two distinct mathematical objects in the same
passage — a terminal object and an identity morphism, a unit element and a
unit map — so the reader cannot determine which referent is in force at
each occurrence. Each symbol has one meaning throughout a page
(`NOT-3`); within a single passage the constraint is tighter, because the
two referents appear side by side.

**Banned:** "Let $\mathcal C$ have finite products and a terminal object
$1$. … $\mu\circ(1\times\zeta)\circ\delta$" — the first $1$ is the
terminal object, the $1$ in $1\times\zeta$ is $\operatorname{id}_c$.

**Preferred:** use distinct symbols. Name the terminal object $e$ or
$\mathbf{1}$, and write $\operatorname{id}_c$ for the identity morphism.
No reader confuses $\operatorname{id}_c\times\zeta$ with
$e\times\zeta$.

### `SYM-5`: A map written without its domain and codomain

A morphism is written as a bare symbol in an equation — $1\times\zeta$,
$\mu\circ\delta$ — without stating its domain and codomain. The reader
must infer the types from context. In a definition, where the reader is
meeting the maps for the first time, state the domain and codomain of
each map before using it in an equation.

**Banned:** "$\mu\circ(1\times\zeta)\circ\delta=\eta\circ{!}_c$" with no
domain or codomain stated for $1\times\zeta$, $\delta$, or $!_c$ before
their use.

**Preferred:** "$\operatorname{id}_c\times\zeta\colon c\times c\to c\times c$,
$\delta\colon c\to c\times c$, and $!_c\colon c\to\mathbf{1}$" stated before the
equations that use them.

### `SYM-6`: A symbol introduced after its first use

A "where" clause defines $\delta$ after $\delta$ has already appeared in
the equations above it. In a definition, every symbol is introduced before
its first use. A "where" clause after an equation is a trailing gloss for
a reader who already knows the notation; it is not a substitute for
stating the data before using it.

**Banned:** equations using $\delta$, then "where
$\delta\colon c\to c\times c$ is the diagonal."

**Preferred:** "Let $\delta\colon c\to c\times c$ be the diagonal and
$!_c\colon c\to\mathbf{1}$ the unique map. Then …" — state the maps,
then write the equations.

## Definitions and statements

### `PR-18`: Patronizing dialectic

The corpus's reader is a graduate student reviewing for a qualifying exam, who
already distinguishes the notions the exam covers. A passage that
manufactures a naive reader — "you might think every continuous bijection is a
homeomorphism, but …" — and then corrects that reader is patronizing. The
corrective positions the author above a reader who needs to be warned; the
precise statement already trusts the reader to understand it.

**Banned:** "One might expect a continuous bijection to have a continuous
inverse, but this requires more."

**Preferred:** "A continuous bijection from a compact space to a Hausdorff
space is a homeomorphism." Where the failure of the tempting converse is
itself worth knowing, give the counterexample as an example block.

### `DEF-15`: One notion per definition block

A `::: {.definition}` block introduces one notion, or one tightly related
family that it enumerates explicitly, such as symmetric, skew-symmetric, and
alternating bilinear forms. A block that defines left modules, right modules,
bimodules, and forgetful functors and closes with a warning about
noncommutative rings is a grab bag, not a definition. A lemma, proposition,
theorem, or remark is never inside a definition block, not even as a trailing
sentence: each statement has its own block with its own logical status, and an
implication between defined notions is a proposition with a proof.

**Banned:** one definition block that defines symmetric, skew-symmetric, and
alternating forms and then asserts "alternating forms are skew-symmetric; the
converse holds when $2$ is invertible."

**Preferred:** a definition block for the three notions, then a
`::: {.proposition}` block stating that alternating forms are skew-symmetric
and that the converse holds when $2$ is a unit, with its proof.

### `SYM-9`: Parallel notions in uniform notation

Parallel notions use parallel notation. Left and right modules, left and
right actions, opposite categories — each pair has two sides that the
reader must distinguish at a glance. Using $A\text{-}\mathbf{Mod}$ for
left modules but $B^{\mathrm{op}}\text{-}\mathbf{Mod}$ for right modules
is inconsistent: the first names the side by position, the second by an
opposite.

**Banned:** "$A\text{-}\mathbf{Mod}$ for left $A$-modules but
$B^{\mathrm{op}}\text{-}\mathbf{Mod}$ for right $B$-modules in the same
passage."

**Preferred:** "$A\text{-}\mathbf{Mod}$ and $\mathbf{Mod}\text{-}A$" for left
and right modules. Choose one convention for sidedness and use it uniformly in
the passage.

### `PR-19`: Logical connective without entailment

A logical connective — "therefore," "hence," "so," "it follows that" —
asserts a consequence. A passage that writes "An $(A,B)$-bimodule
therefore has forgetful functors …" asserts that the bimodule has
forgetful functors as a consequence of the previous line (that a right
module is a left $A^{\mathrm{op}}$-module). The functors are part of the
definition of a bimodule, not a consequence. Do not join a definition to
its own constituent data with a consequence marker.

**Banned:** "A right $A$-module is a left $A^{\mathrm{op}}$-module. An
$(A,B)$-bimodule therefore has forgetful functors …"

**Preferred:** "A right $A$-module is a left $A^{\mathrm{op}}$-module. An
$(A,B)$-bimodule is … It has forgetful functors …" State the definition;
state its data. Use "therefore" only for an actual entailment.

### `DEF-16`: Remark, warning, or example inside a definition block

A definition block defines. A warning, an example, a comparison of alternative
formulations, or a pointer to a subtlety belongs in its own `::: {.remark}` or
`::: {.example}` block after the definition. A definition that contains its
own warning or example cannot be linked or transcluded as the defining
occurrence without dragging them along.

**Banned:** a definition block for modules over a ring whose last sentence is
"For a noncommutative ring, left and right modules must be distinguished."

**Preferred:** close the definition after its defining sentences, then give
the warning in a `::: {.remark}` block.

### `DEF-17`: Reminder masquerading as a definition

"For a ring $A$, write $A\text{-}\mathbf{Mod}$ for the category of left
$A$-modules" does not define left $A$-modules. It assigns notation to a notion
it presupposes: no objects, structure, or morphisms are stated. A definition
states what determines the notion. A reminder says "Recall" and links the
definition card. If the notion is prerequisite, link it; if it is being
defined here, define it.

**Banned:** "For a ring $A$, write $A\text{-}\mathbf{Mod}$ for the category of
left $A$-modules. A right $A$-module is a left $A^{\mathrm{op}}$-module." on a
page that neither defines nor links modules.

**Preferred:** "Recall that a `[[D-…|left $A$-module]]` is …", or a definition
block that defines it.

### `PR-21`: Definition missing "is … if …" and quantifier, redundant qualifier

A property is defined as "finitely generated: some $R^n\twoheadrightarrow M$
is surjective" — no "$M$ is … if …", no quantifier for $M$ or $n$, and a
redundant "is surjective" after $\twoheadrightarrow$, which already means
surjective. A property is stated as "$M$ is $P$ if …" with $M$ bound and the
quantifiers explicit.

**Banned:** "finitely generated: some $R^n\twoheadrightarrow M$ is
surjective" — $M$ unbound, no "is … if …", redundant "is surjective."

**Preferred:** "An $R$-module $M$ is finitely generated if there exist $n\ge0$
and a surjective $R$-linear map $R^n\to M$."

### `SEC-8`: Specialization of a general construction with no new claim

Once a general construction is defined — extension of scalars $B\otimes_A-$
along a ring map $A\to B$ — a sentence that restates it at particular
constants repeats the definition and adds no claim. Use the specialization
inline. If it has a claim of its own, state that claim in an example or
proposition block.

**Banned:** "Extension of scalars along $\mathbb Z\to\mathbb Z_p$ sends a
$\mathbb Z$-module $L$ to $L\otimes_{\mathbb Z}\mathbb Z_p$" as a standalone
sentence.

**Preferred:** write $L\otimes_{\mathbb Z}\mathbb Z_p$ inline; or a
`::: {.proposition}` block with an actual claim, such as "for a finitely
generated $\mathbb Z$-module $L$, the natural map
$L\otimes_{\mathbb Z}\mathbb Z_p\to\varprojlim_n L/p^nL$ is an isomorphism."

### `DEF-21`: Compound term defined by "both conditions hold"

A term "finitely generated projective" is introduced as "both of the first two
conditions hold," referencing bullet order, instead of as the conjunction of
the two defined properties. The compound is not primitive; its meaning is the
conjunction, and any equivalence with another characterization is a theorem.

**Banned:** "finitely generated projective: both of the first two conditions
hold."

**Preferred:** "An $R$-module $M$ is finitely generated projective if it is
finitely generated and projective."

### `PR-22`: "Some … is …" for $\exists$

A property quantified by "there exists" is written as "some
$R^n\twoheadrightarrow M$ is surjective" — colloquial quantification that
picks a morphism $R^n\to M$ and then asks whether that already-surjective
arrow is surjective. Write the quantifier explicitly and do not double the
surjectivity marker.

**Banned:** "finitely generated: some $R^n\twoheadrightarrow M$ is
surjective."

**Preferred:** "there exist $n$ and a surjection $R^n\to M$." State "there
exists" and the surjection once.

### `DEF-22`: Characterization presented as definition

A notion is defined by one characterization and later used through another
whose equivalence is a theorem. When the linked definition card defines
projective modules by the lifting property, "$M$ is a direct summand of a free
module" is the theorem "projective if and only if a direct summand of a free
module", not the definition. Using the characterizations interchangeably hides
the theorem and its hypotheses.

**Banned:** using "direct summand of a free module" as what projective means,
on a page whose linked definition defines projectivity by lifting, with no
reference to the equivalence.

**Preferred:** use the definition the linked card states; when a different
characterization is used, link or state the theorem that proves the
equivalence, with its hypotheses.

## Section structure (`SEC-*`)

A wiki chapter's logical units are its statement blocks — definitions,
theorems, propositions, lemmas, corollaries, examples, and remarks — written
as fenced blocks on cards (`::: {.definition}`, `::: {.theorem}`,
`::: {.example}`, `::: {.remark}`, …) and linked or transcluded by card ID.
Running prose that points at a definition elsewhere, cites a theorem
elsewhere, or paraphrases either is glue between units, not a unit.

### `SEC-1`: A section with no statement block has no content

A section that contains only prose paragraphs — citing a definition, citing a
theorem, then "Hence …" — has no definition, theorem, example, or remark of
its own, and its heading sits over filler. Every section introduces or
transcludes at least one statement block of its own.

**Banned:** "## Creation of limits" followed by five unfenced paragraphs that
cite a definition and a theorem and conclude "Hence a limit of modules is
computed on underlying sets."

**Preferred:** a `::: {.proposition}` block stating that the forgetful functor
from $R$-modules to sets creates limits, with its proof. The paragraphs become
the proof or the remarks after it.

### `SEC-2`: Examples and remarks inside a section are fenced

"For example, …" closing a section, or an aside that two functors "remain
distinct", is an example or remark written as prose. Fence it as a
`::: {.example}` or `::: {.remark}` block.

**Banned:** "For example, the additive and multiplicative monoids of a ring
define distinct functors $\mathbf{Ring}\to\mathbf{Mon}$" as the last sentence
of a section.

**Preferred:** a `::: {.example}` block that states that claim.

### `SEC-3`: Writing requirement inside a mathematical section

A rule about how to write — "a construction whose value agrees on underlying
sets names the functor along which it is created" — does not belong as the
closing moral of a mathematical section. It belongs in this guide.

**Banned:** a prose moral about how to speak of constructions closing a
section on limits.

**Preferred:** state the theorem, prove it, give the example and the
non-example, then close.

### `SEC-4`: Arbitrary breaking of a page into sections

Sections that partition prose to create length or fill a template, rather than
grouping units by logical dependency, are not sections. A section title names
the mathematics its units develop, and its position reflects what those units
use: foundations before the general notions built on them, general notions
before theorems, theorems before applications.

**Banned:** consecutive sections "Creation of limits" and "Parallel functors",
neither with a statement block of its own, the first an application of
monadicity placed before monadicity is available.

**Preferred:** place each unit where its dependencies are satisfied, under a
heading that names what it develops.

### `SEC-5`: A section that is entirely remarks

A section whose only content is remarks, morals, and writing requirements has
no primary claim. A remark is secondary to a definition, theorem, lemma,
proposition, corollary, or example. State the primary claim as the section's
unit and attach the remark to it, or do not create the section.

### `SEC-6`: The skeleton is the statement blocks

The skeleton of a chapter is its statement blocks, each with its hypotheses,
quantifiers, and conclusion. Every term a theorem uses is defined on a linked
definition card, every lemma a proof uses is stated before it or linked, and
every example instantiates a definition. Delete the connecting prose and the
remarks: the remaining blocks must still define every term and state every
claim. If they do not, the chapter is incomplete.

### `SEC-7`: Remarks are for commentary, not for primary claims

A `::: {.remark}` block carries intuition, a warning, or an alternative
viewpoint about the unit it follows. It does not introduce a definition,
theorem, or example of its own. Attach each remark to its primary unit; a
remark with no primary unit does not belong on the page.

## Definitions and links

### `DEF-29`: A definition in running prose is not a definition

A sentence of running prose shaped like a definition — "a factorization of $F$
through $\mathcal D$ consists of …" — is not a definition. It has no card ID,
cannot be linked or transcluded, and is not the defining occurrence (`DEF-1`).
A notion the exposition uses is defined in a `::: {.definition}` block on a
definition card, with its definiendum marked by `\dfn` (`DEF-26`).

**Banned:** a section whose only statement of what "lands in" means is a
sentence of prose.

**Preferred:** a definition card for the notion, linked or transcluded where
it is used.

### `XREF-5`: Link every use of a defined term to its definition card

Every use of a term the corpus defines — "normal family", "Noetherian ring",
"covering space" — that relies on the defined meaning links the term's
definition card: `[[D-IJMPJ|normal family]]`. The link takes the reader to the
precise meaning (`DEF-1`); an unlinked use leaves the reader to guess which
definition applies. This applies to every such use, not only the first.

**Banned:** "a normal family" with no link to its definition card.

**Preferred:** "a `[[D-IJMPJ|normal family]]`".

### `XREF-6`: "Is defined in …; it is …" for recall

"A normal family is defined in `[[D-IJMPJ]]`; it is a family in which …" joins
meta-commentary about where a definition lives to a restatement of it, in two
clauses where one does the work. The standard device for a reminder is
"Recall".

**Banned:** "A normal family is defined in `[[D-IJMPJ]]`; it is a family of
holomorphic functions in which every sequence has a locally uniformly
convergent subsequence."

**Preferred:** "Recall that a `[[D-IJMPJ|normal family]]` is a family of
holomorphic functions in which every sequence has a locally uniformly
convergent subsequence."

### `DEF-30`: Circular definition via a diagram label

The definiendum appears as a label in the diagram that is supposed to define
it: the square's apex is already labeled $f^{-1}(y)$, and the text then says
"the fiber of $f$ over $y$ is the apex". The diagram presupposes the notation
being defined.

**Banned:** a square with apex $f^{-1}(y)$ followed by "The fiber of $f$ over
$y$ is the apex of the cartesian square."

**Preferred:** label the apex neutrally, say $P$, state that the square is a
pullback of $f$ along $y$, and then put $f^{-1}(y):=P$.

### `DEF-31`: "The relevant pullbacks" as a hypothesis

A definition assumes "let $\mathcal{C}$ have a terminal object $1$ and the
relevant pullbacks" without stating which pullbacks are assumed to exist.
"The relevant" names no class of diagrams, and the reader cannot determine
whether the pullback the definition needs exists. State the hypothesis.

**Banned:** "Let $\mathcal{C}$ have a terminal object $1$ and the relevant
pullbacks, let $f\colon X\to Y$, and let $y\colon1\to Y$ be a point."

**Preferred:** "Let $\mathcal{C}$ be a category with terminal object $1$, and
assume the pullback of $f\colon X\to Y$ along $y\colon1\to Y$ exists", or "Let
$\mathcal{C}$ be a category with all pullbacks and a terminal object $1$."

### `PR-27`: Long prose where concise notation already exists

Standard notation — $X\times_Y Z$ for a fiber product,
$\bigoplus_{i\in I}R$ for a free module, a tuple
$(\mathcal{C},\otimes,\mathbf{1})$ for a monoidal category — replaces a
paragraph of English. Spelling out in prose what established notation
already states bloats the text.

**Banned:** "the apex of the cartesian square" for $X\times_Y 1$; "the direct
sum of copies of $R$, one for each element of $I$" repeated where
$\bigoplus_{i\in I}R$ is available.

**Preferred:** "the fiber product $X\times_Y 1$"; "$\bigoplus_{i\in I}R$".

### `TERM-7`: Colloquial or confabulated term in place of a defined one

A term used as if its meaning were obvious, when the corpus defines it nowhere
and an undergraduate would not know it, hides the details it stands for.
Colloquial terms ("apex" for the vertex of a cone, "carries", "identifies
conventions") and confabulated terms that sound technical but have no
referent do the same. Use the standard term and link its definition card
(`XREF-5`); if the corpus has no card for the notion, add one.

**Banned:** "the fiber is the apex of the cartesian square"; "the
discriminant package" (`EV-3`).

**Preferred:** "the fiber is the fiber product $X\times_Y 1$", with the
fiber-product definition card linked.

### `PR-24`: Self-referential meta-prose about the text

Mathematical exposition rarely describes its own structure, notation, or
what its theorems do or do not do; when it must, the note is a one-clause
footnote. Sentences that say where a definition lives ("is defined in
`[[D-…]]`; it is …"), what a theorem does not redefine, what existence does
not supply, what a theorem licenses in notation, or what notation does not
imply are meta-prose, not mathematics. State the mathematics in statement
blocks and link cards; a link is a citation, not self-reference.

**Banned:** "This theorem does not redefine $F$ or $D_P$."; "is additional
data; it does not follow merely from notation."

**Preferred:** the statement block itself, and "Recall that …" with a card
link where a reminder is needed.

### `PR-25`: "Names the …" for specifies/exhibits/is equipped with

"Names" has no established mathematical meaning — nothing in mathematics
"names" anything else. A construction does not "name the functor along which
it is created," "name the comparison," or "name the factorization." The
standard verbs for extra structure each have a clear mathematical meaning:
**specifies** (gives the data), **exhibits** (provides a witness), **is given
by** (is presented as), **is equipped with** / **comes with** (carries as
extra structure), **determines** / **is determined by** (is equivalent to the
data), **is witnessed by**, **is classified by** (when there is a classifying
object).

**Banned:** "names the functor along which it is created"; "names the
comparison with this composite"; "names the factorization"; "names a
particular monomorphism."

**Preferred:** "specifies the functor $\bar F$ and the isomorphism
$\alpha\colon F\cong i\circ\bar F$"; "exhibits the factorization
$(\bar F,\alpha)$"; "is equipped with a chosen monomorphism
$f\colon A\rightarrowtail B$." Use "determines" / "is determined by" only when
the data are equivalent.

### `TERM-6`: Switching terms without stating the identification

"Monomorphism" and "embedding" are used interchangeably in one passage without
defining either or stating how they relate. Choose one term and link its
definition card, or link both and state the relation that holds in the
category at hand.

**Banned:** "some monomorphism $A\to B$ exists … a construction that uses an
embedding" with neither term defined nor related.

**Preferred:** "a monomorphism $f\colon A\rightarrowtail B$ (linked to its
definition card) … in $\mathbf{Set}$, a monomorphism is an injective map."

### `DEF-27`: Distinguished object introduced only in a title

A card titled "Distinguished factorization" that defines factorizations in
general never says which factorization is distinguished. A title is not a
definition. A distinguished, canonical, or standard object is defined as the
chosen object it is, with the construction or comparison that singles it out.

**Banned:** a card titled "Distinguished factorization" whose body defines
only what a factorization is.

**Preferred:** a definition of factorization, then an example block that
states which factorization is distinguished and why.

### `DEF-24`: Property, structure, or existence

"Being a basis" is used without stating whether it is a property of a family,
a chosen structure, or an existence statement. "A basis of $M$ indexed by $I$
is an isomorphism $e\colon R^{(I)}\to M$" collapses the family
$(e(1_i))_{i\in I}$ with the map $e$ and leaves the quantifier ("there exists
$e$" or "a chosen $e$") unstated. State which is meant.

**Preferred:** property — "a family $(m_i)_{i\in I}$ in $M$ is a basis if the
induced map $R^{(I)}\to M$ is an isomorphism"; structure — "a based module is
a pair $(M,e)$ with a chosen isomorphism $e\colon R^{(I)}\to M$"; existence —
"$M$ is free if there exists an isomorphism $R^{(I)}\to M$ for some set $I$."

### `DEF-26`: Mark the term being defined with `\dfn`

In a definition, the term being defined is written `\dfn{term}` at its
defining occurrence. It is never marked with `**bold**`, `*italic*`, or any
other ad hoc emphasis, so every definiendum in the corpus has one style, set in
one place. The surrounding text states the quantifiers and conditions; `\dfn`
marks which word is being introduced. Use `\dfn` only at the defining
occurrence; a later use of the term links its definition card (`XREF-5`).

**Banned:** "An $R$-module $M$ is **torsion** if …"; "An $R$-module $M$ is
*torsion* if …"; "An $R$-module $M$ is torsion if …" with the term unmarked.

**Preferred:**
`Let $R$ be an integral domain. An $R$-module $M$ is \dfn{torsion} if every $m\in M$ is annihilated by some nonzero $r\in R$.`

### `PR-28`: "Requires a theorem with its hypotheses" is not a theorem

Meta-commentary that a conclusion requires a theorem with hypotheses
contributes no statement block to the skeleton (`SEC-6`) and says a theorem
must exist instead of stating it. State the theorem with its hypotheses once,
then apply it.

Vague generality is the other half: "a conclusion about $L$ from either image"
names no conclusion, no images, and no hypotheses, and each possible
conclusion needs different hypotheses.

**Banned:** "A conclusion about $L$ from either image requires a stated
local-to-global theorem with its hypotheses."

**Preferred:** a `::: {.theorem}` block — "A nondegenerate quadratic form over
$\mathbb Q$ represents $0$ nontrivially if and only if it does so over
$\mathbb R$ and over $\mathbb Q_p$ for every prime $p$." — then its
application: "By the Hasse–Minkowski theorem, $q$ is isotropic over
$\mathbb Q$, because …"

### `PR-29`: Vague "either" / "a conclusion" with unquantified hypotheses

"A conclusion," "either image," "some theorem with its hypotheses" are
unbound: no domain, no codomain, no quantifier, no hypothesis list. This is the
general form of `PR-28` and of `PR-22` ("some … is …" for $\exists$): an
English indefinite used for a mathematical quantifier so that no claim is
falsifiable. Each "a" hides a $\forall$ or $\exists$ and a condition.

**Banned:** "A conclusion about $L$ from either image requires a stated
local-to-global theorem with its hypotheses"; "some $R^n\twoheadrightarrow M$
is surjective" (`PR-22`); "the relevant pullbacks" (`DEF-31`).

**Preferred:** "there exist $n$ and a surjective $R$-linear map $R^n\to M$";
"assume $\mathcal C$ has all pullbacks." Write $\forall$/$\exists$ and the
hypothesis list; do not use "a"/"either"/"relevant"/"some" standing for them.

### `PR-30`: Indefinite "a conclusion" with no proposition is unfalsifiable

"A conclusion about $L$" names no proposition: no quantified statement, no
domain, no codomain, no property. Any counterexample can be deflected as "not
the intended conclusion," and any true fact can be claimed afterward as the
intended one. A mathematical sentence is falsifiable because it states which
proposition is claimed; an indefinite noun phrase is not.

This is the general form behind `PR-28`/`PR-29`, `PR-22` ("some
$R^n\twoheadrightarrow M$ is surjective"), and `DEF-31` ("the relevant
pullbacks"): an English indefinite standing for a quantifier so that no
checkable claim is made.

**Banned:** "A conclusion about $L$ from either image requires …"; "A result
about $M$ follows from …"

**Preferred:** state the proposition with its quantifiers: "For a finitely
generated module $M$ over a local ring $R$ with residue field $k$, $M=0$ if
and only if $M\otimes_R k=0$." Name the conclusion; do not use "a conclusion"
or "a result."

### `PR-31`: Tautological "with its hypotheses" does no mathematical work

"With its hypotheses" is true of every stated theorem and adds no hypothesis
list, no condition, and no check. It occupies the grammatical slot where the
hypotheses belong while stating none, so the sentence cannot be used: a reader
cannot verify, apply, or falsify it. It is the same device as "under the
appropriate conditions" or "where defined" standing for the actual conditions.

**Banned:** "requires a stated local-to-global theorem with its hypotheses";
"holds with its hypotheses / under its hypotheses."

**Preferred:** list the hypotheses ("for a nondegenerate quadratic form over
$\mathbb Q$"), or state the theorem that carries them (`PR-28`). If no
specific hypotheses are meant, delete the clause.

### `PR-32`: Contributor governance posing as mathematical content

A sentence whose only coherent audience is a contributor or agent — "requires
a stated theorem," "must be justified," "with its hypotheses" as a reminder to
include them — is contributor governance, not mathematics. On a page it leaks
that governance into the text. Its rhetoric is a preemptive scolding: it
assumes the reader has made, or is about to make, a mistake and corrects it
before it is committed, though the reader never made it. It does not address
the reader as an equal pursuing the mathematics.

Standard mathematical prose never does this. A textbook states the theorem
with its hypotheses, proves it, and applies it; it does not tell the reader
that a theorem or hypothesis is required. The governance belongs in this
guide, not on a page.

This generalizes `PR-24` (self-referential meta-prose) and `PR-18`
(patronizing dialectic).

**Banned:** "A conclusion about $L$ from either image requires a stated
local-to-global theorem with its hypotheses" on a mathematical page; any
sentence that tells the reader that a theorem, proof, or hypothesis is required
instead of giving it.

**Preferred:** on the page, state the mathematics: the theorem block, then "By
the Hasse–Minkowski theorem, …". In this guide, state the governance once:
"Every local-to-global conclusion is a theorem block with quantified
hypotheses."

### `PR-34`: "Without hypothesis $H$" is true of every theorem with hypothesis $H$

"Without the finite-generation hypothesis, $A$ and $B$ differ" is true of any
theorem "$H\Rightarrow A\cong B$" and therefore says nothing: it restates that
the theorem has a hypothesis (`PR-31`) while naming neither the theorem, nor
which finiteness condition is meant, nor the comparison map, so it is
unfalsifiable (`PR-30`).

**Banned:** "Without the finite-generation hypothesis, scalar extension and
completion are distinct constructions."

**Preferred:** state the theorem with its hypothesis and the map, and, where
the boundary teaches something, a counterexample outside the hypothesis: "For
a finitely generated $\mathbb Z$-module $M$, the natural map
$M\otimes_{\mathbb Z}\mathbb Z_p\to\varprojlim_n M/p^nM$ is an isomorphism. For
$M=\mathbb Q$ the source is $\mathbb Q_p$ and the target is $0$."

### `DEF-34`: An unqualified finiteness hypothesis

"The finite-generation hypothesis" names no single notion: finitely generated,
finitely presented, coherent, and perfect are different conditions, and which
one a theorem needs matters. Name the finiteness condition at each use.

**Banned:** "under the finite-generation hypothesis", unqualified.

**Preferred:** "for $M$ finitely presented"; "for $M$ finitely generated over
a Noetherian ring $R$."

### `PR-36`: Negative framing bloats the text, ruins the tone, and undermines standard exposition structure

The general device behind `PR-2`, `PR-24`, `PR-28`, `PR-30`–`PR-32`, and
`PR-34`: instead of the positive quantified statement the mathematics
requires, the text adds a negative sentence — "$a=b$ is a theorem, never a
definitional identity," "does not follow merely from notation," "their mere
existence supplies no order relation," "requires a stated theorem with its
hypotheses," "without $H$, $A$ and $B$ are distinct constructions." Each is a
negation, a "without," or a "requires" standing for a positive definition or
theorem that is not stated.

It has three costs.

**1. Bloat.** A positive theorem has infinitely many true negatives that could
be stated beside it. Stating any of them lengthens the text while adding no
statement block to the skeleton (`SEC-6`). Standard exposition states the
quantified positive once and stops; the complements are evident to a reader
who has read the definitions and the theorem.

**2. Tone.** Each negative assumes a reader who was about to make a mistake
and corrects that mistake before it is made, though the reader never made it
(`PR-32`). Standard prose states the mathematics and lets the reader use it.

**3. Structure.** A negative sentence is not a definition, theorem, or example
with a named map, quantified hypotheses, and a checkable claim. It is
unfalsifiable (`PR-30`), often true by definition or by the logic of "theorems
have hypotheses" (`PR-31`, `PR-34`), and it hides that the actual obligation —
name the map, quantify the hypotheses, give the boundary counterexample when it
teaches — was not met.

**Banned:** "Without the finite-generation hypothesis, scalar extension and
completion are distinct constructions"; "$a=b$ is a theorem, never a
definitional identity"; "does not follow merely from notation"; "is additional
data"; "their mere existence supplies no order relation."

**Preferred:** delete every negative that stands for an unstated positive, and
state the positive once, quantified, with the named map (`PR-34`).

### `PR-50`: Nominalizing the adjective or verb

"Even" is an adjective on a form ($b$ is even); "commutes" and "factors" are
verbs on a diagram. Nominalizing them to "evenness," "injectivity,"
"exactness," "commutativity," or "factorization" plus "condition" forces a
light verb — "satisfies," "has," "exhibits," "possesses" — to re-predicate
them: one checkable predicate becomes three words with no new content, the
same device as "with its hypotheses" (`PR-31`). Use the un-nominalized
predicate.

- **Banned:** "every bilinear form satisfies the evenness condition."
  **Preferred:** "every bilinear form is even."
- **Banned:** "$f$ satisfies the injectivity condition."
  **Preferred:** "$f$ is injective."
- **Banned:** "the sequence satisfies exactness at $M$."
  **Preferred:** "the sequence is exact at $M$."
- **Banned:** "the diagram satisfies the commutativity condition."
  **Preferred:** "the diagram commutes."
- **Banned:** "$b$ satisfies the factorization condition through $N$."
  **Preferred:** "$b$ factors through $N$."

In each case delete the noun, "condition," and the light verb, and keep the
adjective or verb that already is the claim.

### `PR-52`: Weasel mass nouns

"Information," "data," "setting," "condition," "hypotheses," "conclusion,"
"notion," and "structure," used with no fixed referent, exploit colloquial
understanding so a sentence can be defended as true under some interpretation
while naming nothing to check. The problem is detected by what the noun does,
not by a word list.

A clause is weasel-wording when any one of these holds:

- **No fixed referent.** The noun names no defined object: no definition card,
  no type, no stated list.
- **Meaning depends on a context that is never fixed.** "Retains additional
  information" is true of any true statement; "with its hypotheses" is true of
  every theorem; "in the discriminant setting" is true in whatever ambient the
  reader imagines.
- **Unfalsifiable.** Any counterexample can be deflected as "not the intended
  information / setting / condition," because no quantified proposition was
  stated (`PR-30`).
- **Abuse of colloquial understanding.** The reader is expected to supply the
  mathematical meaning from ordinary English.
- **Occupies the slot of a named object.** The noun sits where a map,
  submodule, category, or diagram is owed.

Replace the noun by the object that already has a name:

- **Banned:** "quadratic forms retain more information than their bilinear
  forms."
  **Preferred:** "distinct quadratic forms can have the same associated
  bilinear form: over $\mathbb F_2$, $x^2+xy+y^2$ and $xy$ both have polar
  form $b(u,v)=u_1v_2+u_2v_1$."
- **Banned:** "in the discriminant setting."
  **Preferred:** "for the discriminant form
  $q_L\colon L^\vee/L\to\mathbb Q/2\mathbb Z$ of an even nondegenerate lattice
  $L$."
- **Banned:** "with its hypotheses"; "satisfies the evenness condition."
  **Preferred:** "for $2$ a unit in $R$"; "$b$ is even" (`PR-31`, `PR-50`).

New weasel nouns will appear; audit by the indicators, not the list. When one
is found, replace it by the object that already has a name, or define that
object on a card; do not add the noun to a list and keep the sentence.

### `PR-60`: A construction that chooses data states how it varies with the choice

Choosing an ordered basis, a generating set, a presentation, a base point, or
a trivialization is extra data, not an innocent "let $e$ be …". After a
construction that makes such a choice, state how the result changes when the
choice changes and which invariants do not depend on it.

**Banned:** "the Gram matrix of $b$" or "the fundamental group of $X$" with no
basis or base point named and no statement of how the result depends on it.

**Preferred:** "For an ordered basis $e$ of $M$, put
$G_e(b):=(b(e_i,e_j))_{i,j}$. If $e'=eP$ with $P\in\operatorname{GL}_n(R)$,
then $G_{e'}(b)=P^{t}G_e(b)P$, so $\det G_e(b)$ is well defined up to
multiplication by the square of a unit." Likewise, for a path-connected space
$X$, a path from $x_0$ to $x_1$ induces an isomorphism
$\pi_1(X,x_0)\cong\pi_1(X,x_1)$, determined by the choice of path up to
conjugation.

### `PR-65`: A remark or example with no claim

A block that performs a computation without stating what it shows has almost
no epistemic status: deleting it leaves the skeleton unchanged (`SEC-6`), and a
reader meeting it cannot tell why the calculation is done. An example states
what it is an example of — the universal claim it instantiates or refutes —
and then shows it. A remark follows the unit it remarks on (`SEC-7`).

**Banned:** "**Remark.** The symmetric form on $\mathbb Z^2$ with Gram matrix
$\begin{pmatrix}0&1\\1&0\end{pmatrix}$ has vanishing diagonal and
$b(e_1+e_2,e_1+e_2)=2$."

**Preferred:** a `::: {.example}` block: "A symmetric bilinear form that
vanishes on a basis need not be alternating. On $\mathbb Z^2$ with standard
basis $e_1,e_2$, let $b$ have Gram matrix
$\begin{pmatrix}0&1\\1&0\end{pmatrix}$. Then $b(e_1,e_1)=b(e_2,e_2)=0$, but
$b(e_1+e_2,e_1+e_2)=2\neq0$."

