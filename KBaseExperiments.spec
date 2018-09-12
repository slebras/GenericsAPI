module KBaseExperiments {

    typedef int bool;

     /* Ref to a genome
        @id ws KBaseGenomes.Genome
     */
     typedef string GenomeRef;

     /* Ref to a Tree
        @id ws KBaseTrees.Tree
     */
     typedef string TreeRef;

     /* Ref to a ConditionSet
        @id ws KBaseExperiments.ConditionSet
     */
     typedef string ConditionSetRef;

     /* Ref to a WS object
        @id ws
     */
     typedef string WSRef;

    /*
        Internally this is used to store factor information (without the value term) and also a
        format for returning data in a useful form from get_conditions
        @optional unit unit_ont_id unit_ont_ref value
    */

    typedef structure{
        string factor;
        string factor_ont_ref;
        string factor_ont_id;
        string unit;
        string unit_ont_ref;
        string unit_ont_id;
        string value;
    } Factor;

    /*
     factors - list of supplied factors
     conditions - mapping of condition_labels to a list of factor values in the same order as the factors array
     ontology_mapping_method - One of “User curation”, “Closest matching string”
     @metadata ws ontology_mapping_method as Mapping Method
     @metadata ws length(factors) as Number of Factors
     @metadata ws length(conditions) as Number of Conditions
    */
     typedef structure{
    	mapping<string, list<string>> conditions;
    	list<Factor> factors;
	    string ontology_mapping_method;
     } ConditionSet;

    /*
        This stores categorical values (in which case the unit information will not be used) and
        is also a return format for attributes
        @optional value_ont_ref value_ont_id unit unit_ont_id unit_ont_ref
    */

    typedef structure{
        string value;
        string value_ont_ref;
        string value_ont_id;
        string unit;
        string unit_ont_ref;
        string unit_ont_id;
    } AttributeValue;

    /*
        Internally this is used to store attribute information. Categorical attributes will possess a
        categories field mapping all values. Quantitative attributes should possess unit information
        @optional unit unit_ont_id unit_ont_ref categories
    */

    typedef structure{
        string attribute;
        string attribute_ont_ref;
        string attribute_ont_id;
        string unit;
        string unit_ont_ref;
        string unit_ont_id;
        mapping<string, AttributeValue> categories;
    } Attribute;

    /*
     factors - list of supplied factors
     conditions - mapping of instance_labels to a list of attribute values in the same order as
     the attributes array

     ontology_mapping_method - One of “User curation”, “Closest matching string”

     @metadata ws ontology_mapping_method as Mapping Method
     @metadata ws length(attributes) as Number of Attributes
     @metadata ws length(instances) as Number of Instances
    */
     typedef structure{
    	mapping<string, list<string>> instances;
    	list<Attribute> attributes;
	    string ontology_mapping_method;
     } AttributeMapping;


     /*
        id_to_data_position - simple representation of a cluster, which maps features/conditions of the cluster to the
        row/col index in the data (0-based index).  The index is useful for fast lookup of data
        for a specified feature/condition in the cluster.
        id_to_condition - links to a specific condition in the associated ConditionSet

        @optional id_to_condition
    */
    typedef structure {
        mapping<string, int> id_to_data_position;
        mapping<string, string> id_to_condition;
    } labeled_cluster;

    /*
        A set of clusters, typically generated for a Float2DMatrix wrapper, such as Expression
        data or single feature knockout fitness data.

        clusters - list of clusters
        original_data - pointer to the original data used to make this cluster set
        tree_ref - pointer to the tree associated with this ClusterSet (if any)
        condition_set_ref - pointer to a condition set for this axis (if any)
        genome_ref - pointer to a genome for this axis (if any)

        @metadata ws length(clusters) as n_clusters
        @metadata ws original_data as Source Data
        @metadata ws tree_ref as Associated Tree
        @metadata ws condition_set_ref as Associated Conditions
        @metadata ws genome_ref as Associated Genome

        @optional tree_ref condition_set_ref genome_ref
    */
    typedef structure {
        list<labeled_cluster> clusters;
        mapping<string, string> clustering_parameters;
        WSRef original_data;
        TreeRef tree_ref;
        WSRef condition_set_ref;
        GenomeRef genome_ref;
    } ClusterSet;
};