sql_operate.py�з�װ����һ���������ݿ���࣬��ͨ�������з���
import_data.py���������ݿ���в�������

����Ҫͬһ���������²������ӣ�
���ݿ���������ͣ�SQLserver
���ݿ�host��ip��192.168.0.109
�˿ڣ�1434
��¼�˺ţ�EBook
���룺ebook
database��ebookdata

���ݿ���
PaperAuthorRadius : ��¼���µ�ID,�����Լ�Ȩ�أ��У�PaperID   Author  Radius��
PaperField ����¼������������һ������Ͷ��������У�PaperID   LevelOneField  LevelTwoField��

json���ݲ�ν�����
��һ�㣺count��name��child // count����������������name��ʾ��ͼ���֣�Acmap����child����һ���죩
�ڶ��㣺count��name��color��r��child  // color������ɫ��r����뾶��name��Environmental science����child�����������
�����㣺count��name��color��r��papers // papers�������ģ���childһ���ǡ����顱����name��Waste management��
���Ĳ㣺author��color��r��y��x��ID // y��x����������꣬ID��ʾ���ı��
�������r�Ĵ�С�����ٵ��Ĳ㣨paper���������

��Map�ļм��У������˵�ͼ��Ƭ�����Լ���ͼ���ӵĴ���

PS:ƽʱ�Ҳ��Ὺ�����ݿ⣬�����Ҫ�����Ļ�������ϵ��