# The Unofficial Guide

Edwyn Ortiz — City Guides

---

# Unit 1

## What This Does

For this I picked the City Guides corpus, which covers nine towns. This system takes all of the travel guides' information, and makes it searchable. This system answers questions related to visiting, traveling, eating, and things to look out for in and around these towns.

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size:** Variable, based on .md headings

**Overlap:** None

The city_guides markdown documents are long guides centered on a main topic,
then separated into focused aspects using headings. Useful information is
spread around across the paragraph (or more) that falls under a heading.
An arbitrary character count is sure to cross-contaminate the foci,
so I decided to use the document's structure to break it into chunks.

Going with chunking by heading section and no overlap for now to keep content
focused. If an issue arises where some chunks contain too much noise, 
I can implement a sliding window approach to divide those large chunks
into smaller ones, or even into paragraph-based chunks if appropriate.

<!-- Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `guide_accessibility.md#0` — produced by: `chunker.py::split_documents`

```
Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.
```

**Chunk 2** — source: `guide_corry_vale.md#6` — produced by: `chunker.py::split_documents`

```
When to go

May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and several footpaths become genuinely boggy rather than merely wet. The road is not gritted above the second village and is impassable in snow.
```

**Chunk 3** — source: `guide_givens_mill.md#3` — produced by: `chunker.py::split_documents`

```
Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.
```

**Chunk 4** — source: `guide_kestrelford.md#6` — produced by: `chunker.py::split_documents`

```
When to go

Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters.
```

**Chunk 5** — source: `guide_regional_transport.md#1` — produced by: `chunker.py::split_documents`

```
The railway

The line runs along the river valley, connecting Brightwater to the regional
hub in 50 minutes. Eleven services a day on weekdays, six on Sundays. The line
north of Brightwater closed in 1963 and everything beyond it is bus or car.

Tickets are cheaper booked the day before than on the day, and considerably
cheaper than that booked a week ahead. There is no ticket office at
Brightwater station outside weekday mornings; the machine on the platform takes
cards only.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:** What is there to see in Pellew Sands?

**Answer:**

```
In Pellew Sands, there is a two-mile beach of hard sand (excellent at low tide and unremarkable at high), municipal gardens behind the seafront, and the surviving half of an 1890s pier that is open and free. 

Source: `guide_pellew_sands.md`

Sources retrieved: guide_accessibility.md, guide_eating.md, guide_elder_ness.md, guide_pellew_sands.md
```

**My relevance cutoff:** 0.65

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| Where can I get something to eat and drink in Brightwater? | Yes  | 0.547 |
| Where can I stay while visiting Marchwood? | Yes | 0.457 |
| What is there to see in Pellew Sands? | Yes | 0.317 |
| What should I look out for when traveling by bus? | Yes | 0.617 |
| How can I get around Kestrelford? | Yes | 0.338 |
| What is the capital of Mongolia? | No | 0.767 |
| How do I change the oil in a diesel engine? | No | 0.889 |
| Who won the 1994 World Cup? | No | 0.906 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.838 |
| How do I write a for loop in Rust? | No | 0.852 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** I asked Claude to give me feedback on my acceptance criteria. How they would be tested with only the sentence itself, would two different people score them the same way, and what would have to happen for them to fail. I was able to use the feedback that some of my criteria were vague, and adjust them to be unambiguous.

**2.** I asked Claude to look at my split_documents() implementation, for errors and edge cases. One case, was that my initial function using `chunk_start = doc.text.find("#")` would break if it received a .md file with no headings. The other, was if a heading marker had no non-alphanumeric characters after it to the document end, I would get an out of range IndexError from: 

```
while not doc.text[chunk_start].isalnum():
    chunk_start += 1
```

I hardened the implementation to fix these potential issues. Neither of these would occur from the corpus version used currently, but the system is now more resilent in case more .md documents are added to it.




<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. At least 2 complete, untruncated sentences are gathered for each collected chunk.| 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Average end-to-end latency under 4 seconds | 5 of 5| 4 of 5 | 5 of 5 | 5 of 5 | MISSED |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

### How can I get around Kestrelford?
- Best distance: 0.3377 (passed the gate)
- Total time: 0.8118s
- Retrieval time: 0.1297s 
- Generation time: 0.6820s
- Sources retrieved: guide_accessibility.md, guide_kestrelford.md, guide_regional_transport.md, guide_walking.md

| Chunk # | distance | source | preview |
| 1 | 0.3377 | guide_kestrelford.md | Kestrelford | Kestrelford is a hill town of 12,000, a...|
| 2 | 0.4772 | guide_walking.md | Seasonal notes | Add four minutes to any Brightwater ...|
| 3 | 0.4946 | guide_accessibility.md | Difficult | **Kestrelford** is built on a slope and t... |
| 4 | 0.5103 | guide_regional_transport.md | Driving | Roads are good between the towns and poor o... |
| 5 | 0.5539 | guide_walking.md | Easy, on good surfaces | The **Brightwater river path... |

```
There is no transport within the town of Kestrelford, so you must get around on foot (*guide_accessibility.md*). The street plan has not changed since the 1200s, making it charming on foot and difficult in a car (*guide_kestrelford.md*).
```

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | For at least 4 of my 5 test questions, the retrieved chunks include one that contains the answer | MET | From reading the retrieved chunks, I was able to determine that the answer was among them for each test. |
| 2 | Every answer the system produces names at least one source document | MET | Alongside answers, I was able to see that the system included at least one source document even in cases where the answer was not what I expected. |
| 3 | When I ask a question my documents clearly don't cover, the relevance gate stops it and the system returns "I don't have enough information about that" — in at least 4 of 5 tries | MET | Within the logged data, I was able to verify that each of the out-of-scope questions was blocked by the relevance gate. |
| 4 | At least 2 complete, untruncated sentences are gathered for each collected chunk | MET | Inspecting the retrieved chunks for each test, I was able to verify the met length requirement, and that no chunks were being unintentionally cut short. |
| 5 | The average end-to-end latency of the 5 test questions should be under 4 seconds | MISSED | Across multiple testing runs, end-to-end latency was inconsistent at meeting the criteria. |


## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

For criterion 5, average end-to-end latency isn't a fully trustworthy measure in this system.

Time required to load documents, chunk them, and embed the chunks is only applied to one end-to-end question of one run. This causes average end-to-end latency to be skewed for a run in a way that isn't reflective of the system in every other run. A miss caused by this doesn't say that the system's performance is poor, it only shows that the time to load, chunk, and embed has to be taken somewhere.

Average end-to-end latency's reliability is also diminished when the currently used Gemini model is not fully and immediately available. Any time spent on retries during answer generation is time added to latency, caused by external factors. Availability can directly move the needle but in a way that suggests to run tests at a different time, rather than suggest that the generation process has room for improvement.


## The Improvement

**What I changed:**

I changed what the evaluation measures, not how the pipeline works. `run_eval.py` now has a `warm_up` function that runs one throwaway query before any timing starts. That query is none of my five test questions, and its only job is to make `store.py` load the embedding model and open the Chroma collection, which it otherwise does lazily on the first real search. Every timed run now begins from the same warm state, so the timing table holds retrieval, the gate, and generation and nothing else.

The warm-up time is now written into the run log because it is a real cost. It's reported there as something the process pays once rather than something one question pays on behalf of the other fourteen. Alongside the code change, criterion 5 itself now reads median instead of average, which is written up in `criteria.md`.

**Why I picked it:**

My first diagnosis says the load, chunk, and embed time lands on one question of
one run and skews that run's average, so I have currently moved that time out of the
measurement instead of trying to make it smaller.

The fix had to be to the measurement, because there was nothing wrong with the
system. Loading documents, chunking them, and embedding the chunks is work that
happens once, and a user asking a question of a store that already exists never
waits for it. Counting it inside one query made the system look slower than
anyone actually experiences it, and effort spent making that number smaller
would have been effort spent on a cost no user pays.

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

From `results/run_2026-09-29_1741_after.md`.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. At least 2 complete, untruncated sentences are gathered for each collected chunk. | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Median end-to-end latency under 4 seconds | 5 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |

Criterion 4 carries over between runs. Nothing in this improvement touched `chunker.py` or the chunk settings in `config.py`, so the chunks in the after run are the same chunks as in the before run.

**Did it help?**

Yes, though it is worth being clear about what it fixed and what it did not.

The measurement artifact is gone. In the before run, the first retrieval took 0.456s against a 
0.091s baseline for that same question. In the after run the first retrieval is 0.029s and sits inside the ordinary range of every other retrieval in the log. The 0.489s of setup that used to hide inside that one number is now on its own line where I can read it.

Criterion 5 is met. No single run in the after log went over 4 seconds. The slowest was 1.680s and the median across all fifteen runs was 0.638s.

The code change is not the only reason the criterion is met now, and I don't want to give it more credit than it earned. Revising the criterion from average to median would have carried the before run as well, because the 6.553s that failed it was one run of one question, and that question's median was 0.755s. The warm-up removed a cost that did not belong in the measurement, and the move to median absorbed an outlier the measurement cannot control. Both were needed, and only the first was a change to code.

The system is also not faster. Nothing about retrieval or generation was optimized, and comparing total wall clock between the two runs would be misleading, because they were taken on different days against a service whose speed I don't control.

One thing the change did not fix is that `generate.py` builds its Gemini client lazily, in the same way `store.py` built its embedding model lazily, and that construction happens inside the timed generation block. In the after run the first generation call took 1.650s against a 0.522s baseline for the same question. That is a smaller version of the problem I just fixed, sitting one stage further down the pipeline.

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
