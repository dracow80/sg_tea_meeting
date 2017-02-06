# -*- coding: utf-8 -*-
"""
    Created: 2017-01-31
    LastUpdate: 2017-01-31
    Filename: create_dynamo_table
    Description:
     awscli 를 통해 aws_access_key_id, aws_secret_access_key 등록되어 있다고 가정

    
"""
import boto3
dynamodb = boto3.resource('dynamodb')


def create_achievement_state():
    """
    # 사용자 업적 테이블 AchievementState
    :return: True or False
    """
    table_name = 'AchievementState_test'
    achievement_state = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'user_id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'acv_id',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'user_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'acv_id',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }

    )

    # Wait until the table exists.
    achievement_state.meta.client.get_waiter('table_exists').wait(TableName=table_name)
    return True if achievement_state.item_count == 0 else False


def create_achievement_list():
    """
    # 업적 테이블 AchievementList
    :return:
    """
    table_naem = 'AchievementList'
    achievement_list = dynamodb.create_table(
        TableName=table_naem,
        KeySchema=[
            {
                'AttributeName': 'svc_id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'acv_id',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'svc_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'acv_id',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }

    )

    # Wait until the table exists.
    achievement_list.meta.client.get_waiter('table_exists').wait(TableName=table_naem)
    return True if achievement_list.item_count == 0 else False


if __name__ == '__main__':
    print 'achievement_state: {}'.format(create_achievement_state())
    # print 'achievement_list: {}'.format(create_achievement_list())


