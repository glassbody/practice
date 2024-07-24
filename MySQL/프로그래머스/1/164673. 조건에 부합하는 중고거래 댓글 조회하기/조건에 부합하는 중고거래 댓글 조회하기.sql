-- 코드를 입력하세요
SELECT  USED_GOODS_BOARD.title, USED_GOODS_BOARD.BOARD_ID,
USED_GOODS_REPLY.REPLY_ID, USED_GOODS_REPLY.WRITER_ID, 
USED_GOODS_REPLY.CONTENTS, date_format(USED_GOODS_REPLY.CREATED_DATE,'%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD
inner join used_goods_reply
on USED_GOODS_BOARD.board_id = used_goods_reply.board_id
where used_goods_board.created_date like '2022-10%'
order by used_goods_reply.created_date asc, USED_GOODS_BOARD.TITLE asc;