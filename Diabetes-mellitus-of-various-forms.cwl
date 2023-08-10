cwlVersion: v1.0
steps:
  read-potential-cases-disc:
    run: read-potential-cases-disc.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule1
      potentialCases:
        id: potentialCases
        source: potentialCases
  diabetes---secondary:
    run: diabetes---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule2
      potentialCases:
        id: potentialCases
        source: read-potential-cases-disc/output
  diabetes-mellitus-of-various-forms---secondary:
    run: diabetes-mellitus-of-various-forms---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule3
      potentialCases:
        id: potentialCases
        source: diabetes---secondary/output
  diabetes-mellitus-of-various-forms-ketoacidosis---secondary:
    run: diabetes-mellitus-of-various-forms-ketoacidosis---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule4
      potentialCases:
        id: potentialCases
        source: diabetes-mellitus-of-various-forms---secondary/output
  renal-diabetes-mellitus-of-various-forms---secondary:
    run: renal-diabetes-mellitus-of-various-forms---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule5
      potentialCases:
        id: potentialCases
        source: diabetes-mellitus-of-various-forms-ketoacidosis---secondary/output
  ophthalmic-diabetes-mellitus-of-various-forms---secondary:
    run: ophthalmic-diabetes-mellitus-of-various-forms---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule6
      potentialCases:
        id: potentialCases
        source: renal-diabetes-mellitus-of-various-forms---secondary/output
  neurological-diabetes-mellitus-of-various-forms---secondary:
    run: neurological-diabetes-mellitus-of-various-forms---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule7
      potentialCases:
        id: potentialCases
        source: ophthalmic-diabetes-mellitus-of-various-forms---secondary/output
  diabetes-mellitus-of-various-forms-circulatory---secondary:
    run: diabetes-mellitus-of-various-forms-circulatory---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule8
      potentialCases:
        id: potentialCases
        source: neurological-diabetes-mellitus-of-various-forms---secondary/output
  diabetes-mellitus-of-various-forms-unspecified---secondary:
    run: diabetes-mellitus-of-various-forms-unspecified---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule9
      potentialCases:
        id: potentialCases
        source: diabetes-mellitus-of-various-forms-circulatory---secondary/output
  multiple-diabetes-mellitus-of-various-forms---secondary:
    run: multiple-diabetes-mellitus-of-various-forms---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule10
      potentialCases:
        id: potentialCases
        source: diabetes-mellitus-of-various-forms-unspecified---secondary/output
  diabetes-mellitus-of-various-forms-complication---secondary:
    run: diabetes-mellitus-of-various-forms-complication---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule11
      potentialCases:
        id: potentialCases
        source: multiple-diabetes-mellitus-of-various-forms---secondary/output
  diabetes-mellitus-of-various-forms-malnutritionrelated---secondary:
    run: diabetes-mellitus-of-various-forms-malnutritionrelated---secondary.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule12
      potentialCases:
        id: potentialCases
        source: diabetes-mellitus-of-various-forms-complication---secondary/output
  output-cases:
    run: output-cases.cwl
    out:
    - output
    in:
      inputModule:
        id: inputModule
        source: inputModule13
      potentialCases:
        id: potentialCases
        source: diabetes-mellitus-of-various-forms-malnutritionrelated---secondary/output
class: Workflow
inputs:
  potentialCases:
    id: potentialCases
    doc: Input of potential cases for processing
    type: File
  inputModule1:
    id: inputModule1
    doc: Python implementation unit
    type: File
  inputModule2:
    id: inputModule2
    doc: Python implementation unit
    type: File
  inputModule3:
    id: inputModule3
    doc: Python implementation unit
    type: File
  inputModule4:
    id: inputModule4
    doc: Python implementation unit
    type: File
  inputModule5:
    id: inputModule5
    doc: Python implementation unit
    type: File
  inputModule6:
    id: inputModule6
    doc: Python implementation unit
    type: File
  inputModule7:
    id: inputModule7
    doc: Python implementation unit
    type: File
  inputModule8:
    id: inputModule8
    doc: Python implementation unit
    type: File
  inputModule9:
    id: inputModule9
    doc: Python implementation unit
    type: File
  inputModule10:
    id: inputModule10
    doc: Python implementation unit
    type: File
  inputModule11:
    id: inputModule11
    doc: Python implementation unit
    type: File
  inputModule12:
    id: inputModule12
    doc: Python implementation unit
    type: File
  inputModule13:
    id: inputModule13
    doc: Python implementation unit
    type: File
outputs:
  cases:
    id: cases
    type: File
    outputSource: output-cases/output
    outputBinding:
      glob: '*.csv'
requirements:
  SubworkflowFeatureRequirement: {}
