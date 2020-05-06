
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALL AND BEGIN COMMA CREATE DELETE DIVISION DOT DROP END ENDREQUEST EQUAL FROM GREATER_THAN GREATER_THAN_OR_EQUAL INSERT INTERSECT INTO JOIN LBRACKET LEFT LESS_THAN LESS_THAN_OR_EQUAL MINUS NAME NOT NOT_EQUAL ON OR OUTER PLUS QUOTE RBRACKET RIGHT ROLLBACK SELECT SET SHOW STAR TABLE TRANSACTION UNION UPDATE USING VALUES WHERE bol bool float int strstart : create ENDREQUEST\n             | show ENDREQUEST\n             | drop ENDREQUEST\n             | tree_selects ENDREQUEST\n             | insert ENDREQUEST\n             | update ENDREQUEST\n             | delete ENDREQUEST\n             | transaction ENDREQUESTtransaction : BEGIN TRANSACTION\n                   | END TRANSACTION\n                   | ROLLBACKcreate : CREATE create_bodycreate_body : TABLE NAME LBRACKET variables RBRACKETvariables : NAME type\n              | variables COMMA NAME typeshow : SHOW CREATE TABLE NAMEdrop : DROP TABLE NAMEjoin : JOIN\n            | LEFT OUTER JOIN\n            | RIGHT OUTER JOINjoin_right_table : NAME ON field EQUAL field\n            | NAME USING LBRACKET fields RBRACKET\n            | NAMEunion : UNION\n            | UNION ALLintersect : INTERSECTtree_selects : nested_selectsnested_selects : select\n                    | select union nested_selects\n                    | select intersect nested_selectsselect : SELECT select_body join join_right_table\n              | SELECT select_body join join_right_table condition\n              | SELECT select_body\n              | SELECT select_body conditionselect_body : fields FROM NAME\n                   | STAR COMMA fields FROM NAME\n                   | STAR FROM NAMEinsert : INSERT insert_bodyinsert_body : INTO NAME VALUES LBRACKET values RBRACKET\n                   | INTO NAME LBRACKET fields RBRACKET VALUES LBRACKET values RBRACKETupdate : UPDATE update_bodyupdate_body : NAME SET expression\n                   | NAME SET expression conditionexpression : field EQUAL tree_expression\n                  | expression COMMA field EQUAL tree_expressiondelete : DELETE FROM NAME\n              | DELETE FROM NAME conditionvalues : value\n              | values COMMA valuevalue : NAME\n             | QUOTE NAME QUOTEfields : field\n              | fields COMMA fieldfield : NAME\n            | NAME DOT NAMEcondition : WHERE tree_conditiontree_condition : tree_comparison operator_condition tree_condition\n                        | tree_comparisontree_comparison :  tree_expression operator_comparison tree_expressiontree_expression : value\n            | value operator_expression tree_expression\n            | operator_expression tree_expression\n            | LBRACKET tree_expression RBRACKET\n            | tree_expression operator_expression tree_expressionoperator_condition : AND\n                            | OR operator_comparison : EQUAL\n                            | NOT_EQUAL\n                            | GREATER_THAN\n                            | LESS_THAN\n                            | GREATER_THAN_OR_EQUAL\n                            | LESS_THAN_OR_EQUALoperator_expression : PLUS\n                | MINUS\n                | STAR\n                | DIVISIONtype : int\n            | str\n            | bol\n            | bool\n            | float'
    
_lr_action_items = {'CREATE':([0,11,],[10,32,]),'SHOW':([0,],[11,]),'DROP':([0,],[12,]),'INSERT':([0,],[14,]),'UPDATE':([0,],[15,]),'DELETE':([0,],[16,]),'BEGIN':([0,],[17,]),'END':([0,],[18,]),'ROLLBACK':([0,],[19,]),'SELECT':([0,41,42,43,44,58,],[21,21,21,-24,-26,-25,]),'$end':([1,22,23,24,25,26,27,28,29,],[0,-1,-2,-3,-4,-5,-6,-7,-8,]),'ENDREQUEST':([2,3,4,5,6,7,8,9,13,19,20,30,34,36,39,40,45,47,52,55,56,57,60,71,74,76,77,78,81,82,84,87,93,95,97,102,105,122,132,138,141,142,143,144,145,146,147,149,158,159,160,162,],[22,23,24,25,26,27,28,29,-27,-11,-28,-12,-38,-41,-9,-10,-33,-54,-17,-46,-29,-30,-34,-16,-42,-47,-31,-23,-56,-58,-60,-50,-35,-55,-37,-43,-32,-62,-13,-44,-57,-59,-64,-61,-63,-51,-36,-39,-45,-21,-22,-40,]),'TABLE':([10,12,32,],[31,33,51,]),'INTO':([14,],[35,]),'NAME':([15,21,31,33,35,38,51,54,59,61,64,65,66,67,68,69,70,73,85,86,88,89,90,91,92,100,103,104,106,108,109,110,111,112,113,114,115,116,117,118,119,120,121,125,133,140,150,152,153,157,],[37,47,50,52,53,55,71,47,78,-18,87,93,47,95,47,97,98,47,87,87,124,-73,-74,-75,-76,87,47,87,47,-19,-20,87,-65,-66,87,87,-67,-68,-69,-70,-71,-72,87,147,148,47,87,87,47,87,]),'FROM':([16,46,47,48,49,94,95,96,],[38,65,-54,69,-52,-53,-55,125,]),'TRANSACTION':([17,18,],[39,40,]),'UNION':([20,45,47,60,77,78,81,82,84,87,93,95,97,105,122,141,142,143,144,145,146,147,159,160,],[43,-33,-54,-34,-31,-23,-56,-58,-60,-50,-35,-55,-37,-32,-62,-57,-59,-64,-61,-63,-51,-36,-21,-22,]),'INTERSECT':([20,45,47,60,77,78,81,82,84,87,93,95,97,105,122,141,142,143,144,145,146,147,159,160,],[44,-33,-54,-34,-31,-23,-56,-58,-60,-50,-35,-55,-37,-32,-62,-57,-59,-64,-61,-63,-51,-36,-21,-22,]),'STAR':([21,64,83,84,85,86,87,89,90,91,92,104,110,111,112,113,114,115,116,117,118,119,120,121,122,123,138,142,143,144,145,146,152,158,],[48,91,91,91,91,91,-50,-73,-74,-75,-76,91,91,-65,-66,91,91,-67,-68,-69,-70,-71,-72,91,91,91,91,91,91,91,-63,-51,91,91,]),'SET':([37,],[54,]),'ALL':([43,],[58,]),'JOIN':([45,79,80,93,97,147,],[61,108,109,-35,-37,-36,]),'LEFT':([45,93,97,147,],[62,-35,-37,-36,]),'RIGHT':([45,93,97,147,],[63,-35,-37,-36,]),'WHERE':([45,47,55,74,77,78,84,87,93,95,97,122,138,143,144,145,146,147,158,159,160,],[64,-54,64,64,64,-23,-60,-50,-35,-55,-37,-62,-44,-64,-61,-63,-51,-36,-45,-21,-22,]),'COMMA':([46,47,48,49,74,84,87,94,95,96,99,101,122,126,127,128,129,130,131,134,135,138,143,144,145,146,154,155,156,158,161,],[66,-54,68,-52,103,-60,-50,-53,-55,66,133,66,-62,-14,-77,-78,-79,-80,-81,150,-48,-44,-64,-61,-63,-51,66,-15,-49,-45,150,]),'EQUAL':([47,75,83,84,87,95,122,137,139,143,144,145,146,],[-54,104,115,-60,-50,-55,-62,152,153,-64,-61,-63,-51,]),'RBRACKET':([47,49,84,87,94,95,99,101,122,123,126,127,128,129,130,131,134,135,143,144,145,146,154,155,156,161,],[-54,-52,-60,-50,-53,-55,132,136,-62,145,-14,-77,-78,-79,-80,-81,149,-48,-64,-61,-63,-51,160,-15,-49,162,]),'DOT':([47,],[67,]),'LBRACKET':([50,53,64,72,85,86,89,90,91,92,104,107,110,111,112,113,114,115,116,117,118,119,120,121,151,152,],[70,73,86,100,86,86,-73,-74,-75,-76,86,140,86,-65,-66,86,86,-67,-68,-69,-70,-71,-72,86,157,86,]),'VALUES':([53,136,],[72,151,]),'OUTER':([62,63,],[79,80,]),'QUOTE':([64,85,86,89,90,91,92,100,104,110,111,112,113,114,115,116,117,118,119,120,121,124,150,152,157,],[88,88,88,-73,-74,-75,-76,88,88,88,-65,-66,88,88,-67,-68,-69,-70,-71,-72,88,146,88,88,88,]),'PLUS':([64,83,84,85,86,87,89,90,91,92,104,110,111,112,113,114,115,116,117,118,119,120,121,122,123,138,142,143,144,145,146,152,158,],[89,89,89,89,89,-50,-73,-74,-75,-76,89,89,-65,-66,89,89,-67,-68,-69,-70,-71,-72,89,89,89,89,89,89,89,-63,-51,89,89,]),'MINUS':([64,83,84,85,86,87,89,90,91,92,104,110,111,112,113,114,115,116,117,118,119,120,121,122,123,138,142,143,144,145,146,152,158,],[90,90,90,90,90,-50,-73,-74,-75,-76,90,90,-65,-66,90,90,-67,-68,-69,-70,-71,-72,90,90,90,90,90,90,90,-63,-51,90,90,]),'DIVISION':([64,83,84,85,86,87,89,90,91,92,104,110,111,112,113,114,115,116,117,118,119,120,121,122,123,138,142,143,144,145,146,152,158,],[92,92,92,92,92,-50,-73,-74,-75,-76,92,92,-65,-66,92,92,-67,-68,-69,-70,-71,-72,92,92,92,92,92,92,92,-63,-51,92,92,]),'ON':([78,],[106,]),'USING':([78,],[107,]),'AND':([82,84,87,122,142,143,144,145,146,],[111,-60,-50,-62,-59,-64,-61,-63,-51,]),'OR':([82,84,87,122,142,143,144,145,146,],[112,-60,-50,-62,-59,-64,-61,-63,-51,]),'NOT_EQUAL':([83,84,87,122,143,144,145,146,],[116,-60,-50,-62,-64,-61,-63,-51,]),'GREATER_THAN':([83,84,87,122,143,144,145,146,],[117,-60,-50,-62,-64,-61,-63,-51,]),'LESS_THAN':([83,84,87,122,143,144,145,146,],[118,-60,-50,-62,-64,-61,-63,-51,]),'GREATER_THAN_OR_EQUAL':([83,84,87,122,143,144,145,146,],[119,-60,-50,-62,-64,-61,-63,-51,]),'LESS_THAN_OR_EQUAL':([83,84,87,122,143,144,145,146,],[120,-60,-50,-62,-64,-61,-63,-51,]),'int':([98,148,],[127,127,]),'str':([98,148,],[128,128,]),'bol':([98,148,],[129,129,]),'bool':([98,148,],[130,130,]),'float':([98,148,],[131,131,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'create':([0,],[2,]),'show':([0,],[3,]),'drop':([0,],[4,]),'tree_selects':([0,],[5,]),'insert':([0,],[6,]),'update':([0,],[7,]),'delete':([0,],[8,]),'transaction':([0,],[9,]),'nested_selects':([0,41,42,],[13,56,57,]),'select':([0,41,42,],[20,20,20,]),'create_body':([10,],[30,]),'insert_body':([14,],[34,]),'update_body':([15,],[36,]),'union':([20,],[41,]),'intersect':([20,],[42,]),'select_body':([21,],[45,]),'fields':([21,68,73,140,],[46,96,101,154,]),'field':([21,54,66,68,73,103,106,140,153,],[49,75,94,49,49,137,139,49,159,]),'join':([45,],[59,]),'condition':([45,55,74,77,],[60,76,102,105,]),'expression':([54,],[74,]),'join_right_table':([59,],[77,]),'tree_condition':([64,110,],[81,141,]),'tree_comparison':([64,110,],[82,82,]),'tree_expression':([64,85,86,104,110,113,114,121,152,],[83,122,123,138,83,142,143,144,158,]),'value':([64,85,86,100,104,110,113,114,121,150,152,157,],[84,84,84,135,84,84,84,84,84,156,84,135,]),'operator_expression':([64,83,84,85,86,104,110,113,114,121,122,123,138,142,143,144,152,158,],[85,114,121,85,85,85,85,85,85,85,114,114,114,114,114,114,85,114,]),'variables':([70,],[99,]),'operator_condition':([82,],[110,]),'operator_comparison':([83,],[113,]),'type':([98,148,],[126,155,]),'values':([100,157,],[134,161,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> create ENDREQUEST','start',2,'p_start','SQL_parser.py',284),
  ('start -> show ENDREQUEST','start',2,'p_start','SQL_parser.py',285),
  ('start -> drop ENDREQUEST','start',2,'p_start','SQL_parser.py',286),
  ('start -> tree_selects ENDREQUEST','start',2,'p_start','SQL_parser.py',287),
  ('start -> insert ENDREQUEST','start',2,'p_start','SQL_parser.py',288),
  ('start -> update ENDREQUEST','start',2,'p_start','SQL_parser.py',289),
  ('start -> delete ENDREQUEST','start',2,'p_start','SQL_parser.py',290),
  ('start -> transaction ENDREQUEST','start',2,'p_start','SQL_parser.py',291),
  ('transaction -> BEGIN TRANSACTION','transaction',2,'p_transaction','SQL_parser.py',297),
  ('transaction -> END TRANSACTION','transaction',2,'p_transaction','SQL_parser.py',298),
  ('transaction -> ROLLBACK','transaction',1,'p_transaction','SQL_parser.py',299),
  ('create -> CREATE create_body','create',2,'p_create','SQL_parser.py',310),
  ('create_body -> TABLE NAME LBRACKET variables RBRACKET','create_body',5,'p_create_body','SQL_parser.py',316),
  ('variables -> NAME type','variables',2,'p_variables','SQL_parser.py',322),
  ('variables -> variables COMMA NAME type','variables',4,'p_variables','SQL_parser.py',323),
  ('show -> SHOW CREATE TABLE NAME','show',4,'p_show','SQL_parser.py',334),
  ('drop -> DROP TABLE NAME','drop',3,'p_drop','SQL_parser.py',340),
  ('join -> JOIN','join',1,'p_join','SQL_parser.py',346),
  ('join -> LEFT OUTER JOIN','join',3,'p_join','SQL_parser.py',347),
  ('join -> RIGHT OUTER JOIN','join',3,'p_join','SQL_parser.py',348),
  ('join_right_table -> NAME ON field EQUAL field','join_right_table',5,'p_join_right_table','SQL_parser.py',357),
  ('join_right_table -> NAME USING LBRACKET fields RBRACKET','join_right_table',5,'p_join_right_table','SQL_parser.py',358),
  ('join_right_table -> NAME','join_right_table',1,'p_join_right_table','SQL_parser.py',359),
  ('union -> UNION','union',1,'p_union','SQL_parser.py',369),
  ('union -> UNION ALL','union',2,'p_union','SQL_parser.py',370),
  ('intersect -> INTERSECT','intersect',1,'p_intersect','SQL_parser.py',379),
  ('tree_selects -> nested_selects','tree_selects',1,'p_tree_selects','SQL_parser.py',385),
  ('nested_selects -> select','nested_selects',1,'p_nested_selects','SQL_parser.py',391),
  ('nested_selects -> select union nested_selects','nested_selects',3,'p_nested_selects','SQL_parser.py',392),
  ('nested_selects -> select intersect nested_selects','nested_selects',3,'p_nested_selects','SQL_parser.py',393),
  ('select -> SELECT select_body join join_right_table','select',4,'p_select','SQL_parser.py',405),
  ('select -> SELECT select_body join join_right_table condition','select',5,'p_select','SQL_parser.py',406),
  ('select -> SELECT select_body','select',2,'p_select','SQL_parser.py',407),
  ('select -> SELECT select_body condition','select',3,'p_select','SQL_parser.py',408),
  ('select_body -> fields FROM NAME','select_body',3,'p_select_body','SQL_parser.py',421),
  ('select_body -> STAR COMMA fields FROM NAME','select_body',5,'p_select_body','SQL_parser.py',422),
  ('select_body -> STAR FROM NAME','select_body',3,'p_select_body','SQL_parser.py',423),
  ('insert -> INSERT insert_body','insert',2,'p_insert','SQL_parser.py',434),
  ('insert_body -> INTO NAME VALUES LBRACKET values RBRACKET','insert_body',6,'p_insert_body','SQL_parser.py',440),
  ('insert_body -> INTO NAME LBRACKET fields RBRACKET VALUES LBRACKET values RBRACKET','insert_body',9,'p_insert_body','SQL_parser.py',441),
  ('update -> UPDATE update_body','update',2,'p_update','SQL_parser.py',450),
  ('update_body -> NAME SET expression','update_body',3,'p_update_body','SQL_parser.py',456),
  ('update_body -> NAME SET expression condition','update_body',4,'p_update_body','SQL_parser.py',457),
  ('expression -> field EQUAL tree_expression','expression',3,'p_expression','SQL_parser.py',466),
  ('expression -> expression COMMA field EQUAL tree_expression','expression',5,'p_expression','SQL_parser.py',467),
  ('delete -> DELETE FROM NAME','delete',3,'p_delete','SQL_parser.py',480),
  ('delete -> DELETE FROM NAME condition','delete',4,'p_delete','SQL_parser.py',481),
  ('values -> value','values',1,'p_values','SQL_parser.py',489),
  ('values -> values COMMA value','values',3,'p_values','SQL_parser.py',490),
  ('value -> NAME','value',1,'p_value','SQL_parser.py',501),
  ('value -> QUOTE NAME QUOTE','value',3,'p_value','SQL_parser.py',502),
  ('fields -> field','fields',1,'p_fields','SQL_parser.py',511),
  ('fields -> fields COMMA field','fields',3,'p_fields','SQL_parser.py',512),
  ('field -> NAME','field',1,'p_field','SQL_parser.py',523),
  ('field -> NAME DOT NAME','field',3,'p_field','SQL_parser.py',524),
  ('condition -> WHERE tree_condition','condition',2,'p_condition','SQL_parser.py',533),
  ('tree_condition -> tree_comparison operator_condition tree_condition','tree_condition',3,'p_tree_condition','SQL_parser.py',539),
  ('tree_condition -> tree_comparison','tree_condition',1,'p_tree_condition','SQL_parser.py',540),
  ('tree_comparison -> tree_expression operator_comparison tree_expression','tree_comparison',3,'p_tree_comparison','SQL_parser.py',556),
  ('tree_expression -> value','tree_expression',1,'p_tree_expression','SQL_parser.py',565),
  ('tree_expression -> value operator_expression tree_expression','tree_expression',3,'p_tree_expression','SQL_parser.py',566),
  ('tree_expression -> operator_expression tree_expression','tree_expression',2,'p_tree_expression','SQL_parser.py',567),
  ('tree_expression -> LBRACKET tree_expression RBRACKET','tree_expression',3,'p_tree_expression','SQL_parser.py',568),
  ('tree_expression -> tree_expression operator_expression tree_expression','tree_expression',3,'p_tree_expression','SQL_parser.py',569),
  ('operator_condition -> AND','operator_condition',1,'p_operator_condition','SQL_parser.py',583),
  ('operator_condition -> OR','operator_condition',1,'p_operator_condition','SQL_parser.py',584),
  ('operator_comparison -> EQUAL','operator_comparison',1,'p_operator_comparison','SQL_parser.py',590),
  ('operator_comparison -> NOT_EQUAL','operator_comparison',1,'p_operator_comparison','SQL_parser.py',591),
  ('operator_comparison -> GREATER_THAN','operator_comparison',1,'p_operator_comparison','SQL_parser.py',592),
  ('operator_comparison -> LESS_THAN','operator_comparison',1,'p_operator_comparison','SQL_parser.py',593),
  ('operator_comparison -> GREATER_THAN_OR_EQUAL','operator_comparison',1,'p_operator_comparison','SQL_parser.py',594),
  ('operator_comparison -> LESS_THAN_OR_EQUAL','operator_comparison',1,'p_operator_comparison','SQL_parser.py',595),
  ('operator_expression -> PLUS','operator_expression',1,'p_operator_expression','SQL_parser.py',601),
  ('operator_expression -> MINUS','operator_expression',1,'p_operator_expression','SQL_parser.py',602),
  ('operator_expression -> STAR','operator_expression',1,'p_operator_expression','SQL_parser.py',603),
  ('operator_expression -> DIVISION','operator_expression',1,'p_operator_expression','SQL_parser.py',604),
  ('type -> int','type',1,'p_type','SQL_parser.py',610),
  ('type -> str','type',1,'p_type','SQL_parser.py',611),
  ('type -> bol','type',1,'p_type','SQL_parser.py',612),
  ('type -> bool','type',1,'p_type','SQL_parser.py',613),
  ('type -> float','type',1,'p_type','SQL_parser.py',614),
]
