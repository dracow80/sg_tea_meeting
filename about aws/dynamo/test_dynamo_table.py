# -*- coding: utf-8 -*-
"""
    Created: 2017-02-01
    LastUpdate: 2017-02-01
    Filename: test_dynamo_table
    Description: 
    
"""
import boto3
import uuid
import random
import datetime
dynamodb = boto3.resource('dynamodb')


def insert_achievement_list(svc_id, name, desc, hidden, list_order):
    """
    svc_id : 스토브로부터 발급받은 서비스id(게임id가 될 수 있음) - 유니크해야 됨 (스토브업적: stove_{}, 게임업적: game_{} )
    acv_id : 업적 id - uuid4를 통해 유니크 값 할당

    :param svc_id:
    :param name:
    :param desc:
    :param hidden:
    :param list_order:
    :return:
    """
    # svc_id = 'stove_{}'.format(svc_id)
    acv_id = 'acv_{}'.format(uuid.uuid4())

    table_naem = 'AchievementList'
    table = dynamodb.Table(table_naem)
    return table.put_item(
        Item={
            'svc_id': svc_id,
            'acv_id': acv_id,
            'name': name,
            'desc': desc,
            'hidden': hidden,
            'icon': 'Not yet available',
            'list_order': str(list_order)
        }
    )


def insert_achievement_state(user_id, acv_id, svc_id, complate_dt):
    """
    :param user_id:
    :param acv_id:
    :param svc_id:
    :param complate_dt:
    :return:
    """

    table_naem = 'AchievementState'
    table = dynamodb.Table(table_naem)
    return table.put_item(
        Item={
            'user_id': user_id,
            'acv_id': acv_id,
            'svc_id': svc_id,
            'complate_dt': complate_dt
        }
    )


if __name__ == '__main__':
    # for i in range(20):
    #     print insert_achievement_list('stove_12345',
    #                                   '스토브 테스트 업적 {}'.format(i),
    #                                   '업적 테스트 컨텐츠',
    #                                   'N',
    #                                   random.randint(1, 5))
    #
    # for i in range(20):
    #     print insert_achievement_list('game_0000001',
    #                                   '게임 테스트 업적 {}'.format(i),
    #                                   '업적 테스트 컨텐츠',
    #                                   'N',
    #                                   random.randint(1, 5))

    for i in range(20):
        print insert_achievement_state('user_{}'.format(random.randint(1, 5)),
                                       'acv_{}'.format(uuid.uuid4()),
                                       'stove_12345',
                                       datetime.datetime.utcnow().isoformat(' '))
