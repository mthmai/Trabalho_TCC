#list_columns = ['HUVEC_confidence_value','H1-hESC_confidence_value','GM12878_confidence_value', 
#                        'integrated_confidence_value', 'clinvar_id', 'clinvar_source']

list_columns = ['HUVEC_confidence_value','H1-hESC_confidence_value','GM12878_confidence_value',
                    'integrated_confidence_value', '1000Gp3_AF','1000Gp3_AFR_AF', '1000Gp3_EUR_AF', '1000Gp3_AMR_AF',
                    '1000Gp3_EAS_AF','1000Gp3_SAS_AF', 'gnomAD_exomes_flag', 'gnomAD_exomes_AF','gnomAD_exomes_AFR_AF', 
                    'gnomAD_exomes_AMR_AF', 'gnomAD_exomes_ASJ_AF','gnomAD_exomes_EAS_AF', 'gnomAD_exomes_FIN_AF', 'gnomAD_exomes_NFE_AF',
                    'gnomAD_exomes_SAS_AF', 'clinvar_id', 'clinvar_trait', 'clinvar_var_source']

columns_table_to_search = ['chr','gene_name', 'HGVSc_ANNOVAR', 'HGVSp_ANNOVAR', 'HGVSp_VEP']

columns_table = ['chr', 'pos(1-based)', 'ref', 'alt',	'aaref', 'aaalt', 'rs_dbSNP', 'hg19_chr', 'hg19_pos(1-based)', 'aapos', 'genename', 
                            'HGVSc_ANNOVAR', 'HGVSp_ANNOVAR', 'HGVSp_VEP', 'SIFT_pred', 'SIFT4G_pred', 'Polyphen2_HDIV_pred', 'Polyphen2_HVAR_pred',	'LRT_pred', 
                            'MutationTaster_pred', 'MutationAssessor_pred', 'FATHMM_pred', 'PROVEAN_pred', 'VEST4_score', 'MetaSVM_pred', 'MetaLR_pred', 'MetaRNN_pred', 
                            'MCAP_pred', 'REVEL_score', 'MutPred_score', 'MVP_score', 'MPC_score', 'PrimateAI_pred', 'DEOGEN2_pred', 'BayesDel_addAF_pred', 'BayesDel_noAF_pred',
                            'ClinPred_pred', 'LISTS2_pred', 'CADD_phred', 'CADD_phred_hg19', 'DANN_score', 'fathmmMKL_coding_pred', 'fathmmXF_coding_pred', 'Eigenphred_coding',
                            'EigenPCphred_coding', 'GenoCanyon_score', 'integrated_fitCons_score', 'integrated_confidence_value', 'GM12878_fitCons_score', 'GM12878_confidence_value', 
                            'H1hESC_fitCons_score', 'H1hESC_confidence_value', 'HUVEC_fitCons_score', 'HUVEC_confidence_value', 'LINSIGHT', 'GERP_RS', '1000Gp3_AF', '1000Gp3_AFR_AF', 
                            '1000Gp3_EUR_AF', '1000Gp3_AMR_AF', '1000Gp3_EAS_AF', '1000Gp3_SAS_AF', 'gnomAD_exomes_flag', 'gnomAD_exomes_AF', 'gnomAD_exomes_AFR_AF', 'gnomAD_exomes_AMR_AF', 
                            'gnomAD_exomes_ASJ_AF', 'gnomAD_exomes_EAS_AF', 'gnomAD_exomes_FIN_AF', 'gnomAD_exomes_NFE_AF', 'gnomAD_exomes_SAS_AF', 'clinvar_id', 'clinvar_clnsig', 'clinvar_trait', 
                            'clinvar_var_source']